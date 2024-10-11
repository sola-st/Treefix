# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python
from l3.Runtime import _l_
try:
    import os
    _l_(14660)

except ImportError:
    pass


def files_in_dir(path, extension=''):
    _l_(14664)

    """
       Generator: yields all of the files in <path> ending with
       <extension>

       \param   path       Absolute or relative path to inspect,
       \param   extension  [optional] Only yield files matching this,

       \yield              [filenames]
    """


    for _, dirs, files in os.walk(path):
        _l_(14663)

        dirs[:] = []  # do not recurse directories.
        _l_(14661)  # do not recurse directories.
        yield from [f for f in files if f.endswith(extension)]
        _l_(14662)

# Example: print all the .py files in './python'
for filename in files_in_dir('./python', '*.py'):
    _l_(14666)

    print("-", filename)
    _l_(14665)

path, ext = "./python", ".py"
_l_(14667)
for _, _, dirfiles in os.walk(path):
    _l_(14670)

    matches = (f for f in dirfiles if f.endswith(ext))
    _l_(14668)
    break
    _l_(14669)

for filename in matches:
    _l_(14673)

    print("-", filename)
    _l_(14671)

    matches = [f for f in dirfiles if f.endswith(ext)]
    _l_(14672)

