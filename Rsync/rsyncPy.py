import sys, subprocess
from inspect import getsourcefile
from os.path import dirname, abspath

#Finds parent directory of this script, needed for calling bash files below
parentDir = dirname(abspath(getsourcefile(lambda:0)))

#This function is used for tesing purposes to sync local files
def localRsync(a1,a2,R):
    bashAddr = parentDir + "/Rsync.bash"
    arg = [bashAddr, a1, a2]
    for x in R:
        subprocess.check_call(arg, shell = False)
#This function is called to syn a remote directory 
def remoteRsync(a1,a2,R):
    #Locates bash script in directory
    bashAddr = parentDir + "/Rsync.bash"
    #If the remote locationn responds to ping the rsync bash executes
    if(subprocess.check_call([bashAddr,a2], shell = False) == '0'):
        arg = [bashAddr, a1, a2]
        #For loop for intervals
        for x in R:
            subprocess.check_call(arg, shell = False)
    else:
        print("Error communicating with remote source")
        
#Used for choosing between local or remote
def chooseScript():
    address1 = sys.argv[1]
    address2 = sys.argv[2]
    refreshInterval = sys.argv[3]
    scriptChoice = input("Choose an operating mode:\n1). Local\n2). Remote\n3). Exit\nChoice: ")
    if (scriptChoice == '1'):
        localRsync(address1, address2, refreshInterval)
    elif (scriptChoice == '2'):
        remoteRsync(address1, address2, refreshInterval)
    elif (scriptChoice == '3'):
        return 0
    else:
        print("Invalid Choice\n")
        chooseScript()

    
#Call Stack
if(len(sys.argv) > 3):
    chooseScript()
    
else:
    print("No args")