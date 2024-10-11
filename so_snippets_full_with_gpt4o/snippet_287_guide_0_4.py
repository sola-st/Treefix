from typing import List # pragma: no cover

class MockOS: # pragma: no cover
    def getcwd(self) -> str: # pragma: no cover
        return "/mock/path" # pragma: no cover
 # pragma: no cover
    def listdir(self, directory: str) -> List[str]: # pragma: no cover
        return ["image1.jpg", "image2.jpg"] # pragma: no cover
 # pragma: no cover
mock_glob = type("MockGlob", (object,), { # pragma: no cover
    "glob": lambda self, pattern: ["images/image1.jpg", "images/image2.jpg"] # pragma: no cover
})() # pragma: no cover
 # pragma: no cover
def get_dir_name(f: str) -> str: # pragma: no cover
    return "/mock/path/images" # pragma: no cover
 # pragma: no cover
os = MockOS() # pragma: no cover

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

