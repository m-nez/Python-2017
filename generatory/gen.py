# Copyright (C) 2017 Michał Nieznański
from random import random

print( sum( (random()**2 + random()**2) < 1 for i in range(10000000)) / 10000000 * 4)
