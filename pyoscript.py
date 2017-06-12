#!/usr/bin/env python
from pyo import *
from time import sleep

s = Server(audio='jack')
s.setMidiInputDevice(99)
s.boot().start()

dummy = LFO(freq=0)
dummymidi = Notein()
dummytable = NewTable(length=1, chnls=1)

dummyinput = Input(chnl=0, mul=.7)

table_pyo4e06153256c49c = SndTable("webroot/AKWF_0019.wav")
pyocd2b6bb4e9a09 = SndTable("webroot/AKWF_0008.wav")
pyo53964524ddada4 = SndTable("webroot/AKWF_vgame_0026.wav")

pyo4e06153256c49c = OscTrig(mul = 1, phase = 0, trig = dummy, freq = [0.1]*1, add = 0, table=table_pyo4e06153256c49c)
pyoaa1c0095f95c18 = TrigRand(mul = 1, port = 1, min = 100, input = dummy, init = 110, add = 0, max = 110)
pyof43fd9decf584 = Mixer(outs=2, chnls=10).out()
pyo3276302463575 = Beat(time = 0.5, w1 = 80, w2 = 50, taps = 16, poly = 1, w3 = 30, onlyonce = False).play()
pyoa0f0f8b540dc9 = Allpass(input=[dummy]*10, delay=0, feedback=0, maxdelay=0, mul=0.33)
pyo9b6c493e9f96b8 = Iter(mul = 1, input = dummy, choice = [0.5,0.3,0.2], init = 0, add = 0)
pyo43374e9861e778 = Beat(time = 0.125, w1 = 80, w2 = 50, taps = 16, poly = 1, w3 = 30, onlyonce = False).play()
pyob4690d4b79f8 = Osc(mul = 1, table = dummytable, phase = 0, freq = [0.1]*1, add = 0)
pyo137b26190a5422 = Osc(mul = 1, table = dummytable, phase = 0, freq = [0.1]*1, add = 0)

pyof43fd9decf584.addInput(10,pyo4e06153256c49c)
pyof43fd9decf584.setAmp(10,0,1)
pyof43fd9decf584.setAmp(10,1,1)
pyoa0f0f8b540dc9.input = pyoaa1c0095f95c18
pyob4690d4b79f8.freq = pyoaa1c0095f95c18
pyo137b26190a5422.freq = pyoaa1c0095f95c18
pyoaa1c0095f95c18.input = pyo3276302463575
pyo4e06153256c49c.freq = pyoa0f0f8b540dc9
pyoa0f0f8b540dc9.mul = pyo9b6c493e9f96b8
pyob4690d4b79f8.mul = pyo9b6c493e9f96b8
pyo137b26190a5422.mul = pyo9b6c493e9f96b8
pyo9b6c493e9f96b8.input = pyo43374e9861e778
pyof43fd9decf584.addInput(11,pyob4690d4b79f8)
pyof43fd9decf584.setAmp(11,0,1)
pyof43fd9decf584.setAmp(11,1,1)
pyob4690d4b79f8.table = pyocd2b6bb4e9a09
pyof43fd9decf584.addInput(12,pyo137b26190a5422)
pyof43fd9decf584.setAmp(12,0,1)
pyof43fd9decf584.setAmp(12,1,1)
pyo137b26190a5422.table = pyo53964524ddada4

while True:
	sleep(1)
