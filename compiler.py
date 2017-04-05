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
    fileout.write("s.setMidiInputDevice(99)\n")
    fileout.write("s.boot().start()\n\n")
    
    # general dummy pyobject for init
    fileout.write("dummy = LFO(freq=0)\n\n")
    
    # init pyo objects
    for node in parsed_json:
        if node['type']!='tab':
            # handle special nodes
            # node: out
            #   mixer sending all inputs to sound output -> out()
            if node['type']=='out':
                fileout.write("%s = Mixer(outs=2).out()\n" % (node['id']))
            # ordinary nodes
            else:
                # first compile argument list (arguments start with arg_)
                argumentlist = ""
                for field in node:
                    if(field[:4]=="arg_"):
                        argumentlist += "%s = %s, " % (field[4:], node[field])
            
                # remove trailing ,
                argumentlist = argumentlist.rstrip(', ')
            
                # output object                    
                fileout.write("%s = %s(%s)\n" % (node['id'], node['type'], argumentlist))
            
    fileout.write("\n")
            
    # connect wires
    for node in parsed_json:
        if node['type']!='tab':
            # iterate through "wires" in nodes
            for wire in node['wires']:
                # wire contains all incoming wires per node like [u'pyob32a8810e77fe8', 1, u'ratio', u'b32a8810.e77fe8', 2, u'index', u'b32a8810.e77fe8', 0, u'carrier']
                # split and handle per wire
                subwirelist = list(grouper(3,wire))
                
                for subwire in subwirelist:
                    # find subwire targetobject type
                    targettype = ""
                    for targetnode in parsed_json:
                        if targetnode['type']!='tab' and targetnode['id']==subwire[0]:
                            targettype = targetnode['type']

                    # handle special nodes
                    if targettype == 'out':
                        fileout.write("%s.addInput(%s,%s)\n" % (subwire[0],mixerkey,node['id']))
                        # left and right channel
                        fileout.write("%s.setAmp(%s,0,1)\n" % (subwire[0],mixerkey))
                        fileout.write("%s.setAmp(%s,1,1)\n" % (subwire[0],mixerkey))
                        mixerkey += 1
                    else:
                        #[u'pyo2abb2adff7f916', 0, u'freq']
                        fileout.write("%s.%s = %s\n" % (subwire[0], subwire[2], node['id']))

    fileout.write("\n")
    fileout.write("while True:\n")
    fileout.write("\tsleep(1)\n")
    fileout.close()

# get "last modified" mtime from last modified file in "livepatches"
lasttime_prev = os.stat("./livepatches/" + getfiles("livepatches")[0]).st_mtime

while True:
    lasttime = os.stat("./livepatches/" + getfiles("livepatches")[0]).st_mtime
    if(lasttime!=lasttime_prev):
        print "new file available"
        # read last edited file in livepatches subdir
        thejson = open("./livepatches/" + getfiles("livepatches")[0],"r")
        jsonstring = thejson.read()
        createPyoScript(jsonstring)
        # kill and run pyo script
        try:
          proc
        except NameError:
          pass
        else:
          proc.kill()
        proc = subprocess.Popen("exec ./pyoscript.py",shell=True)
    
        lasttime_prev = lasttime
    
    time.sleep(1)


