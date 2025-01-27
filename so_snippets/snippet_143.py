# Extracted from https://stackoverflow.com/questions/8858008/how-to-move-a-file-in-python
in /opt/awesome
○ → ls
source
○ → ls source
awesome.txt

python 
source = '/opt/awesome/source'
destination = '/opt/awesome/destination'
import os
os.rename(source, destination)
os.listdir('/opt/awesome')
['destination']

import shutil
source = '/opt/awesome/destination' 
destination = '/opt/awesome/source'
shutil.move(source, destination)
os.listdir('/opt/awesome/source')
['awesome.txt']

