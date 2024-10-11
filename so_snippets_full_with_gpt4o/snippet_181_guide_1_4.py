import os # pragma: no cover
import time # pragma: no cover

def get_crtimes_in_dir(directory, raise_on_error=True, as_epoch=False): # pragma: no cover
    # Mock implementation to generate creation time for files # pragma: no cover
    mock_files = ['file1.txt', 'file2.txt', 'file3.txt'] # pragma: no cover
    for fname in mock_files: # pragma: no cover
        date = time.time() if as_epoch else time.ctime(time.time()) # pragma: no cover
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

