import os # pragma: no cover
import glob # pragma: no cover
import imp # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/67631/how-can-i-import-a-module-dynamically-given-the-full-path
from l3.Runtime import _l_
path = os.path.join('./path/to/folder/with/py/files', '*.py')
_l_(14598)
for infile in glob.glob(path):
    _l_(14602)

    basename = os.path.basename(infile)
    _l_(14599)
    basename_without_extension = basename[:-3]
    _l_(14600)

    # http://docs.python.org/library/imp.html?highlight=imp#module-imp
    imp.load_source(basename_without_extension, infile)
    _l_(14601)

