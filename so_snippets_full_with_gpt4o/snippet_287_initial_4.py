import random # pragma: no cover
import tempfile # pragma: no cover

def get_dir_name(file_path):# pragma: no cover
    return os.path.dirname(file_path).split(os.sep)[-1] # pragma: no cover
directory = tempfile.mkdtemp(prefix='images_')# pragma: no cover
# Create placeholder files to simulate images for testing only# pragma: no cover
for i in range(5):# pragma: no cover
    pass

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/10377998/how-can-i-iterate-over-files-in-a-given-directory
from l3.Runtime import _l_
try:
    import glob
    _l_(12883)

except ImportError:
    pass
try:
    import os
    _l_(12885)

except ImportError:
    pass

#to get the current working directory name
cwd = os.getcwd()
_l_(12886)
#Load the images from images folder.
for f in glob.glob('images\*.jpg'):
    _l_(12890)

    dir_name = get_dir_name(f)
    _l_(12887)
    image_file_name = dir_name + '.jpg'
    _l_(12888)
    #To print the file name with path (path will be in string)
    print (image_file_name)
    _l_(12889)

os.listdir(directory)
_l_(12891)

