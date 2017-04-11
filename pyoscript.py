#!/usr/bin/env python
from pyo import *
from time import sleep

s = Server()
s.setMidiInputDevice(99)
s.boot().start()

dummy = LFO(freq=0)
dummymidi = Notein()

hann = HannTable()

pyo852845a4b7976 = Beat(time = 0.125, w1 = 80, w2 = 50, taps = 64, poly = 1, w3 = 80, onlyonce = False).play()
pyo71e93a20c0c894 = TrigRand(mul = 1, port = 0, min = 200, input = dummy, init = 0, add = 0, max = 400)
pyo37c25186a3743e = SumOsc(mul = 1, add = 0, freq = [100]*10, ratio = 0.5, index = 0.5)
pyoc08ab866fde56 = TrigEnv(mul = 1, dur = 0.1, table = hann, add = 0, input = dummy, interp = 1)
pyo334e517ead166e = Allpass(input=[dummy]*10, delay=0, feedback=0, maxdelay=0, mul=1)
pyocca0d08c48771 = Mixer(outs=2, chnls=10).out()
pyo3f7684139de7c4 = CrossFM(mul = 1, ratio = 0.5, ind2 = 2, carrier = 100, ind1 = 2, add = 0)
pyoc0b91c0ba8271 = Allpass(input=[dummy]*10, delay=0, feedback=0, maxdelay=0, mul=0.5)
pyo4dc09ba3abe3fc = Allpass(input=[dummy]*10, delay=0, feedback=0, maxdelay=0, mul=0.25)
pyobea330d10a0f38 = SuperSaw(mul = 1, bal = 0.7, freq = [100]*10, add = 0, detune = 0.5)

pyo71e93a20c0c894.input = pyo852845a4b7976
pyoc08ab866fde56.input = pyo852845a4b7976
pyo37c25186a3743e.freq = pyo71e93a20c0c894
pyoc0b91c0ba8271.input = pyo71e93a20c0c894
pyo334e517ead166e.input = pyo37c25186a3743e
pyo334e517ead166e.mul = pyoc08ab866fde56
pyo3f7684139de7c4.ind2 = pyoc08ab866fde56
pyocca0d08c48771.addInput(10,pyo334e517ead166e)
pyocca0d08c48771.setAmp(10,0,1)
pyocca0d08c48771.setAmp(10,1,1)
pyocca0d08c48771.addInput(11,pyo3f7684139de7c4)
pyocca0d08c48771.setAmp(11,0,1)
pyocca0d08c48771.setAmp(11,1,1)
pyo3f7684139de7c4.carrier = pyoc0b91c0ba8271
pyo4dc09ba3abe3fc.input = pyoc0b91c0ba8271
pyobea330d10a0f38.freq = pyo4dc09ba3abe3fc
pyocca0d08c48771.addInput(12,pyobea330d10a0f38)
pyocca0d08c48771.setAmp(12,0,1)
pyocca0d08c48771.setAmp(12,1,1)

while True:
	sleep(1)
