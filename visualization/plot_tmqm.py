#!/usr/bin/env python3

from read_tmqm import tmqm_properties
import matplotlib.pyplot as plt

plt.hist(tmqm_properties["Electronic_E"], bins=50)

plt.ylabel('Counts')
plt.xlabel('Electronic_E');

plt.show()
