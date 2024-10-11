import os # pragma: no cover
import random # pragma: no cover
from datetime import datetime, timedelta # pragma: no cover

def mock_get_crtimes_in_dir(dir_path, raise_on_error=True, as_epoch=False): # pragma: no cover
    if not os.path.exists(dir_path): # pragma: no cover
        if raise_on_error: # pragma: no cover
            raise FileNotFoundError(f'Path {dir_path} does not exist.') # pragma: no cover
        return # pragma: no cover
    files = [f'file_{i}' for i in range(5)] # pragma: no cover
    for fname in files: # pragma: no cover
        date = datetime.now() - timedelta(days=random.randint(0, 365)) # pragma: no cover
        if as_epoch: # pragma: no cover
            date = int(date.timestamp()) # pragma: no cover
        yield fname, date # pragma: no cover
type('crtime', (object,), {'get_crtimes_in_dir': mock_get_crtimes_in_dir}) # pragma: no cover

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

