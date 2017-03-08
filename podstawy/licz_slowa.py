#!/usr/bin/python
# Copyright (C) 2017 Michał Nieznański

import argparse
from collections import defaultdict
import re

parser = argparse.ArgumentParser(description="Pokaż liczbę poszczególnych słów w pliku")
parser.add_argument("plik")
args = parser.parse_args()

counts = defaultdict(lambda : 0)
with open(args.plik) as f:
    for l in f:
        #for n in (x for x in re.split(r"[^A-Z]+", l.upper()) if x):
        for n in re.findall(r"[A-Z]+", l.upper()):
            counts[n] += 1

for k, v in sorted(counts.items(), key=lambda x: x[1], reverse=True):
    print(k, v)
