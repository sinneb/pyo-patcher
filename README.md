# pyo-patcher
![](http://sinneb.net/pyo-patcher/pyo-patcher-11april.png)

Checkout the [wiki](https://github.com/sinneb/pyo-patcher/wiki/Welcome-to-the-pyo-patcher-wiki) for step by step usage instructions

pyo-patcher is a visual programming environment to create [pyo](http://ajaxsoundstudio.com/software/pyo/) DSP scripts. It runs on a modified version of [Node-RED](https://nodered.org/): flow-based programming for the Internet of Things. This modified version allows, among others, multiple inputs, does not save states (for multiuser online use) and displays port names. The pyo flows are almost Node-RED standard JSON file exports, which, upon download, are picked up by a local Python compiler script. The compiler translates the JSON flow to a pyo script and runs it. The download - compile - run cycle typically takes less than a second to run, which provides almost-instant feedback to the user. 

Check it out! You have to run pyo-patcher yourself, the online version is not available anymore. Have "compiler.py" running on your system and point your browser download location to the "livepatches" subfolder. Compiler.py watches this folder for new files.

As of now (9th april) there is a nice number of generators available, two effects, MIDI possibilities and a new arithmetic function (multiple).

##Local install
- Install Node-RED
- grab the pyo-patcher repo (git clone https://github.com/sinneb/pyo-patcher.git)
- Change to the pyo-patcher dir (cd pyo-patcher)
- Find your local Node-RED install and its red.min.js file (find /. -name red.min.js)
- Overwrite that file (cp node-red-changes/red.js /usr/local/lib/node_modules/node-red/public/red/red.min.js). The modified file is not minified, but the default install uses this file.
- Copy the pyo nodes to the local Node-RED folder (cp -r nodes/ ~/.node-red/)
- Run Node-RED (node-red)
- Open the menu and click "Manage palette". Disable all but "node-red". Open the nodes under "node-red" and disable the non-pyo ones (all the not capitalized ones, but "out"). Once I move the pyo nodes to their own library, this process will become a lot easier.
- Start the local "compiler.py" (python compiler.py)
- Refresh your browser, build something interesting and hit "Deploy". The current flow will be downloaded, picked up, compiled and run.
