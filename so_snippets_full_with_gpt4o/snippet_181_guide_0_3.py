import os # pragma: no cover
import time # pragma: no cover
from typing import List, Tuple # pragma: no cover

def mock_get_crtimes_in_dir(directory: str, raise_on_error: bool, as_epoch: bool) -> List[Tuple[str, str]]: # pragma: no cover
    files = os.listdir(directory) # pragma: no cover
    crtimes = [(file, time.ctime(os.path.getctime(file))) for file in files] # pragma: no cover
    return crtimes # pragma: no cover
type('Mock', (object,), {'get_crtimes_in_dir': mock_get_crtimes_in_dir}); # pragma: no cover

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

