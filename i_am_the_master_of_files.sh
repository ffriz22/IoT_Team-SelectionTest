#!/bin/bash

: '
Franco Friz Rodriguez

i am the master of files.sh
The script will create a file in the directory with the name specified in the filename 
variable and remove the public read rights. (For the owner or the owners group the default 
permissions will remain the same).The contents of the file will be as follows, replacing 
{{uuid}} with the value specified in the uuid input:
'
#adding text with variables and create the file
echo $'[FILE]\nfolder = ./uploads\nid = '$2$'\nslots = 2' > $1
#Others without reading permission
chmod o-r $1