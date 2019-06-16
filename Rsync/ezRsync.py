import sys, subprocess
from inspect import getsourcefile
from os.path import dirname, abspath
import os
import numpy as np
"""
Created on Thu Mar 14 15:19:34 2019

@author: Garvan
"""

def rsync():
    parentDir = dirname(abspath(getsourcefile(lambda:0)))
    print(parentDir)
    print("\nPassowrd: remon\n")
    arg = ["sudo rsync -avh pi@192.168.1.104:/home/pi/Documents/FlightData/Rsync/DataReceived/ /mnt/d/Rocketry/TestEnv/ReceivedData/"]
    subprocess.check_call(arg, shell = True)


def displayData():
    dataDir = '/mnt/d/Rocketry/TestEnv/ReceivedData/'
    print(dataDir)
    for root, dirs, files in os.walk(dataDir): 
        for file in files:  
            if file.endswith(".npy"): 
                currFile = np.load(dataDir + file)
                outputData(currFile)
            
            
def outputData(data):
    print(data[0])


displayData()