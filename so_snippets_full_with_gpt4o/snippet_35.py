# Extracted from https://stackoverflow.com/questions/6996603/how-can-i-delete-a-file-or-folder-in-python
import os
import glob

files = glob.glob(os.path.join('path/to/folder/*'))
files = glob.glob(os.path.join('path/to/folder/*.csv')) // It will give all csv files in folder
for file in files:
    os.remove(file)

from shutil import rmtree
import os


for dirct in os.listdir(os.path.join('path/to/folder')):
    rmtree(os.path.join('path/to/folder',dirct))

