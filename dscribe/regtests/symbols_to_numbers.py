import sys
import unittest

from dscribe.utils.species import symbols_to_numbers

from numpy import array
import ase.data

class UtilsTests(unittest.TestCase):
    def test_symbols_to_atomic_number(self):
        """Tests that chemical symbols are correctly transformed into atomic
        numbers.
        """
        for chemical_symbol in ase.data.chemical_symbols[1:]:
            atomic_number = symbols_to_numbers([chemical_symbol])
            true_atomic_number = ase.data.chemical_symbols.index(chemical_symbol)
            self.assertEqual(atomic_number, true_atomic_number)

    def test_one_level_nested_symbols_to_atmoic_number(self):
        """Test that nested lists work in test_symbols_to_atomic_number"""
        nested_atomic_numbers = symbols_to_numbers(['Al', 'Si', ['Ar', 'H', 'K']])
        self.assertTrue((nested_atomic_numbers==array([13, 14, [18, 1, 19]],dtype=object)).all())

    def test_multiple_levels_nested_symbols_to_atmoic_number(self):
        """Test that nested lists work in test_symbols_to_atomic_number"""
        nested_atomic_numbers = symbols_to_numbers(['Al', 'Si', ['Ar', 'H', ['C', ['Ne']], 'K']])
        self.assertTrue((nested_atomic_numbers==array([13, 14, [18, 1, [6, [10]], 19]],dtype=object)).all())


if __name__ == '__main__':

    suites = []
    suites.append(unittest.TestLoader().loadTestsFromTestCase(UtilsTests))
    alltests = unittest.TestSuite(suites)
    result = unittest.TextTestRunner(verbosity=0).run(alltests)

    # We need to return a non-zero exit code for the gitlab CI to detect errors
    sys.exit(not result.wasSuccessful())
