import os # pragma: no cover
import time # pragma: no cover

def get_crtimes_in_dir(directory, raise_on_error=True, as_epoch=False): # pragma: no cover
    # Mock implementation of get_crtimes_in_dir # pragma: no cover
    for fname in os.listdir(directory): # pragma: no cover
        if not fname.startswith('.'):  # Skip hidden files # pragma: no cover
            crt_time = time.time()  # Use the current time for simplicity # pragma: no cover
            yield fname, crt_time if as_epoch else time.ctime(crt_time) # pragma: no cover

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

