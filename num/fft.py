#!/usr/bin/python
# Copyright (C) 2017 Michał Nieznański
import scipy.io.wavfile
import numpy
from sys import argv

if len(argv) > 1:
    filename = argv[1]
else:
    print("Usage: ", argv[0], "filename")
    exit(1)

sample_rate, data = scipy.io.wavfile.read(filename)
n = len(data)
freq = numpy.fft.fft(data)
freq0 = 1 / (len(data) / sample_rate)
print("Dominating frequency: %dHz" % (freq[:n // 2].argmax() * freq0))

with open("spectrum.txt", "w") as f:
    f.write("\n".join("%g %g" % (i * freq0, abs(c * 2)) for i, c in enumerate(freq[:n // 2])))

stdev = numpy.std(freq)
excluded = 0
for c in numpy.nditer(freq, op_flags=["readwrite"]):
    if abs(c) < stdev:
        c[...] = 0
        excluded += 1
print("Excluded %g%% of harmonics" % (100 * excluded / n))
inverse = numpy.array(numpy.fft.ifft(freq), dtype=data.dtype)
scipy.io.wavfile.write("filtered.wav", sample_rate, inverse)
