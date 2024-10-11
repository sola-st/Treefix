import os # pragma: no cover
import tempfile # pragma: no cover
from datetime import datetime # pragma: no cover

def get_crtimes_in_dir(directory, raise_on_error=True, as_epoch=False): # pragma: no cover
    files = os.listdir(directory) # pragma: no cover
    for f in files: # pragma: no cover
        path = os.path.join(directory, f) # pragma: no cover
        if os.path.isfile(path): # pragma: no cover
            crtime = os.path.getctime(path) # pragma: no cover
            if not as_epoch: # pragma: no cover
                crtime = datetime.fromtimestamp(crtime).strftime('%Y-%m-%d %H:%M:%S') # pragma: no cover
            yield f, crtime # pragma: no cover
temp_dir = tempfile.TemporaryDirectory() # pragma: no cover
with open(os.path.join(temp_dir.name, 'test_file.txt'), 'w') as temp_file: # pragma: no cover
    temp_file.write('This is a test file.') # pragma: no cover
os.chdir(temp_dir.name) # pragma: no cover

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

