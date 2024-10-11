import os # pragma: no cover
from datetime import datetime # pragma: no cover

def get_crtimes_in_dir(dir_path, raise_on_error=False, as_epoch=False): # pragma: no cover
    try: # pragma: no cover
        files = os.listdir(dir_path) # pragma: no cover
    except Exception as e: # pragma: no cover
        if raise_on_error: # pragma: no cover
            raise e # pragma: no cover
        else: # pragma: no cover
            return [] # pragma: no cover
    crtimes = [] # pragma: no cover
    for f in files: # pragma: no cover
        crtime = os.path.getctime(os.path.join(dir_path, f)) # pragma: no cover
        date = datetime.fromtimestamp(crtime) if not as_epoch else crtime # pragma: no cover
        crtimes.append((f, date)) # pragma: no cover
    return crtimes # pragma: no cover

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

