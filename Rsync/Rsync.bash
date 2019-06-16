#!/bin/bash
# rsync script
# exit when any command fails
# -a means archive mode essentailly a default copy mode for rsync
# -v implies verbose meaning that the status of the transfer is displayed
# -c is checksum checks to see if files have changed
# -h is human readable
#- z compresses data
#-P useful for long transfer interruption protection
rsync -chavzP --stats $1 $2