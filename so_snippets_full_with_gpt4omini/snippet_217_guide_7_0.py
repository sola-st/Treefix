import os # pragma: no cover

os.walk = lambda path: iter([('./python', [], ['file1.py', 'file2.py'])]) # pragma: no cover
path = './python' # pragma: no cover
ext = '.py' # pragma: no cover
dirfiles = ['file1.py', 'file2.py', 'other.txt'] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python
from l3.Runtime import _l_
try:
    import os
    _l_(2955)

except ImportError:
    pass


def files_in_dir(path, extension=''):
    _l_(2959)

    """
       Generator: yields all of the files in <path> ending with
       <extension>

       \param   path       Absolute or relative path to inspect,
       \param   extension  [optional] Only yield files matching this,

       \yield              [filenames]
    """


    for _, dirs, files in os.walk(path):
        _l_(2958)

        dirs[:] = []  # do not recurse directories.
        _l_(2956)  # do not recurse directories.
        yield from [f for f in files if f.endswith(extension)]
        _l_(2957)

# Example: print all the .py files in './python'
for filename in files_in_dir('./python', '*.py'):
    _l_(2961)

    print("-", filename)
    _l_(2960)

path, ext = "./python", ".py"
_l_(2962)
for _, _, dirfiles in os.walk(path):
    _l_(2965)

    matches = (f for f in dirfiles if f.endswith(ext))
    _l_(2963)
    break
    _l_(2964)

for filename in matches:
    _l_(2968)

    print("-", filename)
    _l_(2966)

    matches = [f for f in dirfiles if f.endswith(ext)]
    _l_(2967)

