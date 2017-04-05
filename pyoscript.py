#!/usr/bin/env python
from pyo import *
from time import sleep

s = Server().boot()
s.start()
pyo9805f5cd82aa08 = Mixer(outs=2).out()
pyob32a8810e77fe8 = FM(mul = 1, index = 5, ratio = 0.5, carrier = 200, add = 0)
pyoe2ea1254cac28 = Blit(mul = 100, harms = 40, freq = 100, add = 200)

pyo9805f5cd82aa08.addInput(10,pyob32a8810e77fe8)
pyo9805f5cd82aa08.setAmp(10,0,1)
pyo9805f5cd82aa08.setAmp(10,1,1)
pyob32a8810e77fe8.carrier = pyoe2ea1254cac28

while True:
	sleep(1)
