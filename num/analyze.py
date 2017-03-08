#!/usr/bin/python
# Copyright (C) 2017 Michał Nieznański
from sys import argv
from analyzer import SpectrumAnalyzer

if len(argv) > 1:
    filename = argv[1]
else:
    print("Usage: ", argv[0], "filename")
    exit(1)

sa = SpectrumAnalyzer(filename)
sa.export_spectrum("spectrum.txt")
sa.export_filtered("filtered.txt")
print("Dominating frequency: %dHz" % sa.dominating_freq())
