import os # pragma: no cover
from datetime import datetime # pragma: no cover

def get_crtimes_in_dir(directory, raise_on_error=False, as_epoch=False): # pragma: no cover
    crtimes = [] # pragma: no cover
    for filename in os.listdir(directory): # pragma: no cover
        path = os.path.join(directory, filename) # pragma: no cover
        try: # pragma: no cover
            crtime = os.path.getctime(path) # pragma: no cover
            if as_epoch: # pragma: no cover
                crtimes.append((filename, crtime)) # pragma: no cover
            else: # pragma: no cover
                crtimes.append((filename, datetime.fromtimestamp(crtime))) # pragma: no cover
        except Exception as e: # pragma: no cover
            if raise_on_error: # pragma: no cover
                raise e # pragma: no cover
    return crtimes # pragma: no cover

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

