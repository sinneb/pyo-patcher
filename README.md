# pyo-patcher
![](http://sinneb.net/pyo-patcher/pyo-patcher-5april.png)

pyo-patcher is a visual programming environment to create [pyo](http://ajaxsoundstudio.com/software/pyo/) DSP scripts. It runs on a modified version of [Node-RED](https://nodered.org/): flow-based programming for the Internet of Things. This modified version exports pyo flows in JSON files, which, upon download, are picked up by a local Python compiler script. The compiler translates the JSON flow to a pyo script and runs it. The download - compile - run cycle typically takes less than a second to run, which provides almost-instant feedback to the user. 

Check it out! You can run pyo-patcher yourself, or use an online version at http://pyopatcher.sinneb.net. Have  "compiler.py" running on your system and point your browser download location to the "livepatches" subfolder. Compiler.py watches this folder for new files.

As of now (9th april) there is a nice number of generators available, two effects, MIDI possibilities and a new arithmetic function (multiple).

