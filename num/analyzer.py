#!/usr/bin/python
# Copyright (C) 2017 Michał Nieznański

import scipy.io.wavfile
import numpy

class SpectrumAnalyzer:
    def __init__(self, filename, verbose=False):
        self.verbose = False

        self._sample_rate, self._data = scipy.io.wavfile.read(filename)
        self._n = len(self._data)
        self._freq = numpy.fft.fft(self._data)
        self._freq0 = 1 / (self._n / self._sample_rate)

    def export_filtered(self, filename, mult=1):
        stdev = numpy.std(self._freq)
        excluded = 0
        for c in numpy.nditer(self._freq, op_flags=["readwrite"]):
            if abs(c) < stdev * mult:
                c[...] = 0
                excluded += 1

        if self.verbose: print("Excluded %g%% of harmonics" % (100 * excluded / n))
        inverse = numpy.array(numpy.fft.ifft(self._freq), dtype=self._data.dtype)
        scipy.io.wavfile.write("filtered.wav", self._sample_rate, inverse)
    
    def export_spectrum(self, filename):
        with open("spectrum.txt", "w") as f:
            f.write(
                    "\n".join("%g %g" % (i * self._freq0, abs(c * 2))
                        for i, c in enumerate(self._freq[:self._n // 2]))
                )

    def dominating_freq(self):
        return self._freq[:self._n // 2].argmax() * self._freq0
