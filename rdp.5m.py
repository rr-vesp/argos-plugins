#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

#strings to translate
strOpenApp="Otevřít všechna spojení"

from os import listdir
from os.path import isfile, join
from pathlib import Path

homeDir = str(Path.home())

fdir = homeDir + "/.local/share/remmina/"

def getconnection(file):
    connection = fdir + file
    x = file.split("_")
    connection = x[0] + " - " + x[2]
    return x

files = sorted(listdir(fdir))
#files.sort

print ("<span color='#EEE' weight='bold'></span> | iconName=remmina-connect-symbolic")
print ("---")

qDom = "test"
qCounter = 0

for cnFile in files:
    if "remmina" in cnFile:
        
        # display connections in groups, only group GROUP display as top level
        cnData = getconnection(cnFile)
        if (not(cnData[0].upper() == "GROUP")):
            if (not(qDom == cnData[0].upper())):
                print (cnData[0].upper())
            print ("-- " + cnData[2].upper() + "| bash='remmina -c " + fdir + cnFile + "' terminal=false iconName=remmina-" + cnData[1] + "-symbolic")
        else:
            print (cnData[2].upper() + "| bash='remmina -c " + fdir + cnFile + "' terminal=false iconName=remmina-" + cnData[1] + "-symbolic")
        qDom = cnData[0].upper()
        qCounter = qCounter + 1
        #print (":horse:")

print ("---")

#print ("Přidat nové spojení | bash='remmina --new-note' terminal=false iconName=list-add-symbolic")
print ("<span weight='bold'>"+strOpenApp+"</span> | bash='remmina' terminal=false iconName=remmina-panel")
