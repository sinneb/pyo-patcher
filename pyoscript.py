#!/usr/bin/env python
from pyo import *
from time import sleep

s = Server()
s.setInOutDevice(3)
s.setMidiInputDevice(99)
s.boot().start()

dummy = LFO(freq=0)
dummymidi = Notein()

hann = HannTable()
harm = HarmTable()
log = LogTable()
para = ParaTable()
partial = PartialTable()
saw = SawTable(order=32)
sinc = SincTable()
atan = AtanTable()
padsynth = PadSynthTable()
tuckey = WinTable(type=7)
bartlett = WinTable(type=3)
coslog = CosLogTable([(0,0), (4095,1), (8192,0)])
t1 = SndTable("amen.wav")

pyoc698691df2b68 = Pointer2(mul = 1, table = t1, add = 0, interp = 4, index = dummy)
pyoa001ff1082b3d = TrigRand(mul = 1, port = 0.5, min = 0.2, input = dummy, init = 0, add = 0, max = 0.3)
pyo2a517be80f0e5c = Metro(time = 0.5, poly = 1).play()
pyo20a69a6d2a8d06 = Mixer(outs=2, chnls=10).out()

pyo20a69a6d2a8d06.addInput(10,pyoc698691df2b68)
pyo20a69a6d2a8d06.setAmp(10,0,1)
pyo20a69a6d2a8d06.setAmp(10,1,1)
pyoc698691df2b68.index = pyoa001ff1082b3d
pyoa001ff1082b3d.input = pyo2a517be80f0e5c

while True:
	sleep(1)
