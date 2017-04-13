#!/usr/bin/env python

import json, sys, os, time, subprocess, itertools

def getfiles(dirpath):
    a = [s for s in os.listdir(dirpath)
         if os.path.isfile(os.path.join(dirpath, s))]
    a.sort(key=lambda s: os.path.getmtime(os.path.join(dirpath, s)),reverse=True)
    return a

def grouper(n, iterable, fillvalue=None):
    args = [iter(iterable)] * n
    return itertools.izip_longest(fillvalue=fillvalue, *args)

def createPyoScript(jsonstring):
    # unique mixerkeys
    mixerkey = 10;

    # open output file for writing
    fileout = open("pyoscript.py","w") 

    parsed_json = json.loads(jsonstring)

    # fix id's - remove . and prepend with pyo (vars can't start with numbers)
    for node in parsed_json:
        if node['type']!='tab':
            node['id'] = "pyo" + node['id'].replace(".","")
            # remove . in wires
            for wire in node['wires']:
                # check for multiple subwires
                for it in range(0,len(wire)/3):
                    wire[it*3] = "pyo" + wire[it*3].replace(".","")

    # pyo header
    fileout.write("#!/usr/bin/env python\n")
    fileout.write("from pyo import *\n")
    fileout.write("from time import sleep\n")
    fileout.write("\n")
    fileout.write("s = Server()\n")
    fileout.write("s.setInOutDevice(3)\n")
    fileout.write("s.setMidiInputDevice(99)\n")
    fileout.write("s.boot().start()\n\n")
    
    # general dummy pyobject for init
    fileout.write("dummy = LFO(freq=0)\n")
    fileout.write("dummymidi = Notein()\n\n")
    
    # tables
    fileout.write("hann = HannTable()\n")
    fileout.write("harm = HarmTable()\n")
    fileout.write("log = LogTable()\n")
    fileout.write("para = ParaTable()\n")
    fileout.write("partial = PartialTable()\n")
    fileout.write("saw = SawTable(order=32)\n")
    fileout.write("sinc = SincTable()\n")
    fileout.write("atan = AtanTable()\n")
    fileout.write("padsynth = PadSynthTable()\n")
    fileout.write("tuckey = WinTable(type=7)\n")
    fileout.write("bartlett = WinTable(type=3)\n")
    fileout.write("coslog = CosLogTable([(0,0), (4095,1), (8192,0)])\n")
    
    # first write all tables to pyoscript
    for node in parsed_json:
        if node['type']!='tab':
            if node['type']=='SndTable':
                fileout.write("%s = SndTable(\"%s\")\n" % (node['arg_tablename'], node['arg_path']))
                
    fileout.write("\n")
        
    # write init for other pyo objects
    for node in parsed_json:
        if node['type']!='tab':
            
            # build argument list
            argumentlist = ""
            for field in node:
                if(field[:4]=="arg_"):
                    if (field[4:]=="freq"):
                        # reserve 10 streams for poly
                        argumentlist += "%s = [%s]*10, " % (field[4:], node[field])
                    else:
                        argumentlist += "%s = %s, " % (field[4:], node[field])
        
            # remove trailing , and space
            argumentlist = argumentlist.rstrip(', ')
            
            # handle special nodes
            # node: out
            #   mixer sending all inputs to sound output -> out()
            if node['type']=='out':
                # mixer chnls should match the poly on notein (which is max 10)
                fileout.write("%s = Mixer(outs=2, chnls=10).out()\n" % (node['id']))
            elif node['type']=='Multiply':
                fileout.write("%s = Allpass(input=[dummy]*10, delay=0, feedback=0, maxdelay=0, mul=%s)\n" % (node['id'], node['arg_mult']))
            elif node['type']=='SndTable':
                pass
            elif node['type']=='Metro':
                fileout.write("%s = %s(%s).play()\n" % (node['id'], node['type'], argumentlist))
            elif node['type']=='Beat':
                fileout.write("%s = %s(%s).play()\n" % (node['id'], node['type'], argumentlist))
            elif node['type']=='Cloud':
                fileout.write("%s = %s(%s).play()\n" % (node['id'], node['type'], argumentlist))
            elif node['type']=='Euclide':
                fileout.write("%s = %s(%s).play()\n" % (node['id'], node['type'], argumentlist))
            elif node['type']=='Seq':
                fileout.write("%s = %s(%s).play()\n" % (node['id'], node['type'], argumentlist))
            # ordinary nodes
            else:
                # output object                    
                fileout.write("%s = %s(%s)\n" % (node['id'], node['type'], argumentlist))
            
    fileout.write("\n")

    # connect wires
    for node in parsed_json:
        # print "---"
        # print node['type']
        # print node

        if node['type']!='tab':
            
            # detect multiple wires (e.g. this node has multiple outs)    
            wireID = 0;
            # iterate through "wires" in nodes
            for wire in node['wires']:
                
                # handle special nodes
                currentNodeID = node['id']
                if node['type']=='Notein':
                    if wireID==0:
                        currentNodeID = node['id']+"['pitch']"
                    if wireID==1:
                        currentNodeID = node['id']+"['velocity']"
                    
                # wire contains all outgoing wires per node like [u'pyob32a8810e77fe8', 1, u'ratio', u'b32a8810.e77fe8', 2, u'index', u'b32a8810.e77fe8', 0, u'carrier']
                # destination node id, destination portnumber, destination port name.
                # split and handle per wire
                subwirelist = list(grouper(3,wire))
            
                for subwire in subwirelist:
                    # find destination node type
                    destinationNodeType = ""
                    for destNode in parsed_json:
                        if destNode['type']!='tab' and destNode['id']==subwire[0]:
                            destinationNodeType = destNode['type']

                    # handle special nodes
                    if destinationNodeType == 'out':
                        fileout.write("%s.addInput(%s,%s)\n" % (subwire[0],mixerkey,currentNodeID))
                        # left and right channel
                        fileout.write("%s.setAmp(%s,0,1)\n" % (subwire[0],mixerkey))
                        fileout.write("%s.setAmp(%s,1,1)\n" % (subwire[0],mixerkey))
                        mixerkey += 1
                    elif destinationNodeType == 'Multiply':
                        if subwire[2] == 'in':
                            fileout.write("%s.input = %s\n" % (subwire[0],currentNodeID))
                        if subwire[2] == 'mult':
                            fileout.write("%s.mul = %s\n" % (subwire[0],currentNodeID))
                    else:
                        #[u'pyo2abb2adff7f916', 0, u'freq']
                        fileout.write("%s.%s = %s\n" % (subwire[0], subwire[2], currentNodeID))
                    
                wireID+=1;

    fileout.write("\n")
    fileout.write("while True:\n")
    fileout.write("\tsleep(1)\n")
    fileout.close()

# get "last modified" mtime from last modified file in "livepatches"
lasttime_prev = os.stat("./livepatches/" + getfiles("livepatches")[0]).st_mtime

while True:
    lasttime = os.stat("./livepatches/" + getfiles("livepatches")[0]).st_mtime
    if(lasttime!=lasttime_prev):
        print "compiling new patch"
        # read last edited file in livepatches subdir
        thejson = open("./livepatches/" + getfiles("livepatches")[0],"r")
        jsonstring = thejson.read()
        createPyoScript(jsonstring)
        # kill and run pyo script
        print "running..."
        try:
          proc
        except NameError:
          pass
        else:
          proc.kill()
        proc = subprocess.Popen("exec ./pyoscript.py",shell=True)
    
        lasttime_prev = lasttime
    
    time.sleep(1)


