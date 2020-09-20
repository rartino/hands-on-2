#!/usr/bin/env python3
import numpy
from numpy.lib.recfunctions import append_fields

#def read_xyzlist(filename):
#
#    def xyz_lines_to_atoms(lines):
#        s = "".join(lines)
#        sf = io.StringIO(s)
#        return ase.io.read(sf, format="xyz")
#
#    f = open("tmQM_X.xyz", "r")
#    all_structures = []
#    lines = []
#    for line in f:
#        if line == "\n":
#            all_structures.append(xyz_lines_to_atoms(lines))
#            lines = []
#        else:
#            lines.append(line)
#    all_structures.append(xyz_lines_to_atoms(lines))
#    f.close()

def read_xyzlist_formulas(filename):
    f = open("tmQM_X.xyz", "r")
    formulas = []
    for line in f:
        if line.startswith("CSD_code"):
            fields = line.split("|")
            sto = fields[3]
            formula = sto.partition("=")[2].strip()
            formulas.append(formula)
    f.close()
    return numpy.array(formulas,dtype=str)

tmqm_properties = numpy.genfromtxt('tmQM_y.csv', delimiter=';',names=True, dtype=None, encoding="utf-8")
formulas = read_xyzlist_formulas("tmQM_X.xyz")
tmqm_properties = append_fields(tmqm_properties, 'formula', data=formulas)

# Available properties columns: CSD_code, Electronic_E, Dispersion_E, Dipole_M, Metal_q, HL_Gap, HOMO_Energy, LUMO_Energy, Polarizability, formula
