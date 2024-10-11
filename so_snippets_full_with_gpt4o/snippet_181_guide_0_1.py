import os # pragma: no cover
import datetime # pragma: no cover

def get_crtimes_in_dir(path, raise_on_error=False, as_epoch=True): # pragma: no cover
    for entry in os.scandir(path): # pragma: no cover
        if entry.is_file(): # pragma: no cover
            creation_time = entry.stat().st_ctime # pragma: no cover
            if not as_epoch: # pragma: no cover
                creation_time = datetime.datetime.fromtimestamp(creation_time) # pragma: no cover
            yield entry.name, creation_time # pragma: no cover

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

