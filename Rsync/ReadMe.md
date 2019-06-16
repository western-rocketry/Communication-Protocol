# What is Rsync?
Rsync is a linux bash tool which allows for folder and file transfer between two connected devices. It is more advantageous to normal
methods of file transfer as it only transfers files which are different or not currentlt avaiable in the destination directory.
This is specifically valuable for us as it means our bandwith usage will be minimal. 

## Rsync.bash
This file is the bash command to call Rsync between two file locations and is called programatially from the Python script ezRsync.py

## ezRsync.py 
This file performs Rsync between two raspberry pi directories over a wifi connection.

## numpyRand.py 
This file creates test data used for tranfer, although meaningless it is in the same format as the real data.

## ping.bash 
This file is used to test the connection between two ip addresses prior to file transfer

## rsyncPy.py 
This will be the final control file for all rsync functionalilty but is not complete.

