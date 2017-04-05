#!/usr/bin/env python
from pyo import *
from time import sleep

s = Server()
s.setMidiInputDevice(99)
s.boot().start()

dummy = LFO(freq=0)

pyo32f21fda1926f = Mixer(outs=2).out()
pyob37bced3d5fca = Freeverb(size = 0.7, mul = 1, damp = 1, bal = 0.5, input = dummy, add = 0)
pyo49427769567128 = FM(mul = 1, index = 5, ratio = 0.5, carrier = 100, add = 0)
pyo3d7d708f1daaf = ChenLee(mul = 1, chaos = 0.1, add = 0, pitch = 0.1)
pyod4cc8724128018 = Midictl(mul = 1, channel = 0, minscale = 0, maxscale = 50, init = 10, add = 0, ctlnumber = 100)
pyoc7acdc6df4752 = Midictl(mul = 1, channel = 0, minscale = 20, maxscale = 1000, init = 100, add = 0, ctlnumber = 101)

pyo32f21fda1926f.addInput(10,pyob37bced3d5fca)
pyo32f21fda1926f.setAmp(10,0,1)
pyo32f21fda1926f.setAmp(10,1,1)
pyob37bced3d5fca.input = pyo49427769567128
pyo49427769567128.ratio = pyo3d7d708f1daaf
pyo49427769567128.index = pyod4cc8724128018
pyo49427769567128.carrier = pyoc7acdc6df4752

while True:
	sleep(1)
