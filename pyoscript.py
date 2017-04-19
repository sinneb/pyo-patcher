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

pyocdd574d5b8405 = LFO(mul = 0.5, type = 2, freq = [1]*10, add = 0.5, sharp = 1)
pyof6437c7c597148 = Mixer(outs=2, chnls=10).out()
pyo7eadf560241c1c = Midictl(mul = 1, channel = 0, minscale = 0, maxscale = 10, init = 1, add = 0, ctlnumber = 100)
pyo6c676aea17a1e4 = Midictl(mul = 1, channel = 0, minscale = 0, maxscale = 1, init = 0, add = 0, ctlnumber = 101)
pyo233044ba59aac4 = Midictl(mul = 1, channel = 0, minscale = 0, maxscale = 100, init = 1, add = 0, ctlnumber = 102)
pyob2f7a4ec11fa18 = SumOsc(mul = 1, add = 0, freq = [100]*10, ratio = 0.5, index = 0.5)
pyoc39b227222139 = Allpass(input=[dummy]*10, delay=0, feedback=0, maxdelay=0, mul=1)
pyoed25cd2ce1793 = TrigEnv(mul = 1, dur = 1, table = hann, add = 0, input = dummy, interp = 1)
pyo24f65751f88ae8 = Allpass(input=[dummy]*10, delay=0, feedback=0, maxdelay=0, mul=1)
pyo36dbd5e7e7a082 = Metro(time = 1, poly = 1).play()
pyo1120f2fb5a0945 = Midictl(mul = 1, channel = 0, minscale = 0, maxscale = 10, init = 1, add = 0, ctlnumber = 103)
pyo49f7e99ecd1d18 = Midictl(mul = 1, channel = 0, minscale = 0, maxscale = 10, init = 1, add = 0, ctlnumber = 104)
pyo830b6ff6c4af48 = Midictl(mul = 1, channel = 0, minscale = 0, maxscale = 1, init = 1, add = 0, ctlnumber = 105)
pyod8e67da73192d = Midictl(mul = 1, channel = 0, minscale = 0, maxscale = 1, init = 0.5, add = 0, ctlnumber = 106)
pyoe20f29fb0bd7a = Midictl(mul = 1, channel = 0, minscale = 0, maxscale = 20, init = 0.5, add = 0, ctlnumber = 107)
pyodcaa3ec2fbe578 = Euclide(time = 0.125, taps = 16, poly = 1, onsets = 10).play()
pyo53acc5dd45e55c = TrigRand(mul = 1, port = 0.1, min = 60, input = dummy, init = 100, add = 0, max = 220)
pyo882644a747baa = Midictl(mul = 1, channel = 0, minscale = 0, maxscale = 10, init = 1, add = 0, ctlnumber = 108)
pyo563da885c93cc8 = Midictl(mul = 1, channel = 0, minscale = 20, maxscale = 400, init = 100, add = 0, ctlnumber = 109)
pyoc72c16febbb = Midictl(mul = 1, channel = 0, minscale = 20, maxscale = 700, init = 200, add = 0, ctlnumber = 110)
pyodb79e7184f0318 = CrossFM(mul = 1, ratio = 0.5, ind2 = 2, carrier = 100, ind1 = 2, add = 0)
pyo45a6166f08b998 = Midictl(mul = 1, channel = 0, minscale = 0, maxscale = 1, init = 0.5, add = 0, ctlnumber = 111)
pyob8005affe53c28 = Midictl(mul = 1, channel = 0, minscale = 0, maxscale = 10, init = 2, add = 0, ctlnumber = 112)
pyodd4573bccdad98 = Midictl(mul = 1, channel = 0, minscale = 0, maxscale = 10, init = 2, add = 0, ctlnumber = 113)
pyo729e6471e02ddc_mixer = Mixer(outs=2, chnls=10)
pyo729e6471e02ddc = pyo729e6471e02ddc_mixer[0] + pyo729e6471e02ddc_mixer[1]
pyo20c61f1dc4598 = MoogLP(mul = 1, res = 0, input = dummy, freq = [1000]*10, add = 0)
pyo422f05586617d4 = Delay(mul = 1, maxdelay = 5, input = dummy, delay = 0.25, add = 0, feedback = 0)
pyo7171d4e164c404 = Midictl(mul = 1, channel = 0, minscale = 20, maxscale = 1000, init = 1000, add = 0, ctlnumber = 114)
pyo1d0d63c4e7fffc = Midictl(mul = 1, channel = 0, minscale = 0, maxscale = 2, init = 0, add = 0, ctlnumber = 115)

pyo24f65751f88ae8.input = pyocdd574d5b8405
pyoc39b227222139.input = pyo7eadf560241c1c
pyocdd574d5b8405.sharp = pyo6c676aea17a1e4
pyoc39b227222139.mul = pyo233044ba59aac4
pyo729e6471e02ddc_mixer.addInput(10,pyob2f7a4ec11fa18)
pyo729e6471e02ddc_mixer.setAmp(10,0,1)
pyo729e6471e02ddc_mixer.setAmp(10,1,1)
pyocdd574d5b8405.freq = pyoc39b227222139
pyo24f65751f88ae8.mul = pyoed25cd2ce1793
pyob2f7a4ec11fa18.mul = pyo24f65751f88ae8
pyodb79e7184f0318.mul = pyo24f65751f88ae8
pyoed25cd2ce1793.input = pyo36dbd5e7e7a082
pyo36dbd5e7e7a082.time = pyo1120f2fb5a0945
pyoed25cd2ce1793.dur = pyo49f7e99ecd1d18
pyoed25cd2ce1793.mul = pyo830b6ff6c4af48
pyob2f7a4ec11fa18.index = pyod8e67da73192d
pyob2f7a4ec11fa18.ratio = pyoe20f29fb0bd7a
pyo53acc5dd45e55c.input = pyodcaa3ec2fbe578
pyob2f7a4ec11fa18.freq = pyo53acc5dd45e55c
pyodb79e7184f0318.carrier = pyo53acc5dd45e55c
pyodcaa3ec2fbe578.time = pyo882644a747baa
pyo53acc5dd45e55c.min = pyo563da885c93cc8
pyo53acc5dd45e55c.max = pyoc72c16febbb
pyo729e6471e02ddc_mixer.addInput(11,pyodb79e7184f0318)
pyo729e6471e02ddc_mixer.setAmp(11,0,1)
pyo729e6471e02ddc_mixer.setAmp(11,1,1)
pyodb79e7184f0318.ratio = pyo45a6166f08b998
pyodb79e7184f0318.ind1 = pyob8005affe53c28
pyodb79e7184f0318.ind2 = pyodd4573bccdad98
pyo20c61f1dc4598.input = pyo729e6471e02ddc
pyo422f05586617d4.input = pyo20c61f1dc4598
pyof6437c7c597148.addInput(12,pyo422f05586617d4)
pyof6437c7c597148.setAmp(12,0,1)
pyof6437c7c597148.setAmp(12,1,1)
pyo20c61f1dc4598.freq = pyo7171d4e164c404
pyo20c61f1dc4598.res = pyo1d0d63c4e7fffc

while True:
	sleep(1)
