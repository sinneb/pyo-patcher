#!/usr/bin/env python
from pyo import *
from time import sleep

s = Server()
s.setMidiInputDevice(99)
s.boot().start()

dummy = LFO(freq=0)
dummymidi = Notein()

hann = HannTable()

pyoc4191e265656c8 = Seq(time = 1, onlyonce = False, poly = 1, seq = [2,1,1,2]).play()
pyob115b1dd2656e = Iter(mul = 1, input = dummy, choice = [300, 350, 400, 450, 500, 550], init = 0, add = 0)
pyodcc7d99e117888 = SumOsc(mul = 1, add = 0, freq = [100]*10, ratio = 0.5, index = 0.5)
pyod5bbdd8e2cce08 = Metro(time = 1, poly = 1).play()
pyofb773e8867fcb8 = Mixer(outs=2, chnls=10).out()
pyo5a8de239b23ad4 = Allpass(input=[dummy]*10, delay=0, feedback=0, maxdelay=0, mul=0.5)
pyo2198025ff7fe16 = SumOsc(mul = 1, add = 0, freq = [100]*10, ratio = 0.5, index = 0.5)
pyo9356ae81d7f97 = Degrade(mul = 1, srscale = 0.5, input = dummy, add = 0, bitdepth = 4)

pyob115b1dd2656e.input = pyoc4191e265656c8
pyodcc7d99e117888.freq = pyob115b1dd2656e
pyo5a8de239b23ad4.input = pyob115b1dd2656e
pyo9356ae81d7f97.input = pyodcc7d99e117888
pyoc4191e265656c8.time = pyod5bbdd8e2cce08
pyo2198025ff7fe16.freq = pyo5a8de239b23ad4
pyo9356ae81d7f97.input = pyo2198025ff7fe16
pyofb773e8867fcb8.addInput(10,pyo9356ae81d7f97)
pyofb773e8867fcb8.setAmp(10,0,1)
pyofb773e8867fcb8.setAmp(10,1,1)

while True:
	sleep(1)
