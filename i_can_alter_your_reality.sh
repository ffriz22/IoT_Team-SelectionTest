#!/bin/bash

: '
Franco Friz Rodriguez

The script will access the file with the name specified in the filename 
variable, search for all fields with an id name and replace their value
with that of the uuid variable.
'
#Replace id section with argument $2 in the document $1
sed -i '/id/ c id = '$2 $1 