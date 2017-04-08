#!/usr/bin/env python
from pyo import *
from time import sleep

s = Server()
s.setMidiInputDevice(99)
s.boot().start()

dummy = LFO(freq=0)
dummymidi = Notein()

pyo87d473092646e = Mixer(outs=2, chnls=10).out()
pyof9a44edaaaf7d = SuperSaw(mul = 1, bal = 0.7, freq = [100]*10, add = 0, detune = 0.5)
pyob450c47f0adc48 = Notein(mul = 1, channel = 0, first = 0, add = 0, poly = 10, scale = 1, last = 127)
pyo2f11226c248e3e = Phasor(mul = 10, phase = 0, freq = [0.1]*10, add = 0)
pyo9c2eb6d5d51798 = LFO(mul = 1, type = 7, freq = [10]*10, add = 0, sharp = 1)
pyo3772e92e9aa9a6 = MidiAdsr(mul = 1, sustain = 0.7, input = dummymidi['velocity'], attack = 0.01, release = 1, add = 0, decay = 0.05)
pyo2e4c8660a1241a = Allpass(input=[dummy]*10, delay=0, feedback=0, maxdelay=0, mul=1)
pyofbccea05860878 = Mixer(outs=2, chnls=10).out()

pyo2e4c8660a1241a.input = pyof9a44edaaaf7d
pyof9a44edaaaf7d.freq = pyob450c47f0adc48['pitch']
pyo3772e92e9aa9a6.input = pyob450c47f0adc48['velocity']
pyof9a44edaaaf7d.detune = pyo2f11226c248e3e
pyof9a44edaaaf7d.bal = pyo9c2eb6d5d51798
pyo2e4c8660a1241a.mul = pyo3772e92e9aa9a6
pyofbccea05860878.addInput(10,pyo2e4c8660a1241a)
pyofbccea05860878.setAmp(10,0,1)
pyofbccea05860878.setAmp(10,1,1)

while True:
	sleep(1)
