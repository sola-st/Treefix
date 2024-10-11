import os # pragma: no cover
import time # pragma: no cover

def get_crtimes_in_dir(path, raise_on_error=False, as_epoch=True): # pragma: no cover
    for fname in os.listdir(path): # pragma: no cover
        if as_epoch: # pragma: no cover
            date = time.time() # pragma: no cover
        else: # pragma: no cover
            date = time.ctime() # pragma: no cover
        yield fname, date # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/237079/how-do-i-get-file-creation-and-modification-date-times
from l3.Runtime import _l_
try:
    from crtime import get_crtimes_in_dir
    _l_(14595)

except ImportError:
    pass

for fname, date in get_crtimes_in_dir(".", raise_on_error=True, as_epoch=False):
    _l_(14597)

    print(fname, date)
    _l_(14596)

