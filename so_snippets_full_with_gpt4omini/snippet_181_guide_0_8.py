from datetime import datetime # pragma: no cover
import os # pragma: no cover

def get_crtimes_in_dir(directory, raise_on_error=False, as_epoch=False): # pragma: no cover
    result = [] # pragma: no cover
    for filename in os.listdir(directory): # pragma: no cover
        path = os.path.join(directory, filename) # pragma: no cover
        ctime = os.path.getctime(path) # pragma: no cover
        if as_epoch: # pragma: no cover
            result.append((filename, ctime)) # pragma: no cover
        else: # pragma: no cover
            result.append((filename, datetime.fromtimestamp(ctime))) # pragma: no cover
    return result # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/237079/how-do-i-get-file-creation-and-modification-date-times
from l3.Runtime import _l_
try:
    from crtime import get_crtimes_in_dir
    _l_(2858)

except ImportError:
    pass

for fname, date in get_crtimes_in_dir(".", raise_on_error=True, as_epoch=False):
    _l_(2860)

    print(fname, date)
    _l_(2859)

