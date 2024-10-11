import os # pragma: no cover
from datetime import datetime # pragma: no cover

def get_crtimes_in_dir(directory, raise_on_error=True, as_epoch=False): # pragma: no cover
    if not os.path.isdir(directory): # pragma: no cover
        if raise_on_error: # pragma: no cover
            raise ValueError('Directory does not exist') # pragma: no cover
        return # pragma: no cover
    files = os.listdir(directory) # pragma: no cover
    result = [] # pragma: no cover
    for f in files: # pragma: no cover
        path = os.path.join(directory, f) # pragma: no cover
        if os.path.isfile(path): # pragma: no cover
            crtime = os.path.getctime(path) # pragma: no cover
            if not as_epoch: # pragma: no cover
                crtime = datetime.fromtimestamp(crtime).strftime('%Y-%m-%d %H:%M:%S') # pragma: no cover
            result.append((f, crtime)) # pragma: no cover
    return result # pragma: no cover
sys.modules['crtime'] = type('Mock', (object,), {'get_crtimes_in_dir': get_crtimes_in_dir}) # pragma: no cover

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

