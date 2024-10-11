import os # pragma: no cover
import time # pragma: no cover

def get_crtimes_in_dir(directory, raise_on_error=True, as_epoch=False): # pragma: no cover
    # Mock implementation of get_crtimes_in_dir # pragma: no cover
    def create_time(file): # pragma: no cover
        return time.ctime(os.path.getctime(file)) if not as_epoch else os.path.getctime(file) # pragma: no cover
    try: # pragma: no cover
        files = os.listdir(directory) # pragma: no cover
        if not files: # pragma: no cover
            raise FileNotFoundError('No files found in the directory') # pragma: no cover
        return [(f, create_time(os.path.join(directory, f))) for f in files] # pragma: no cover
    except Exception as e: # pragma: no cover
        if raise_on_error: # pragma: no cover
            raise e # pragma: no cover
        else: # pragma: no cover
            return [] # pragma: no cover
mocked_dir_path = '.' # pragma: no cover
mocked_files = ['file1.txt', 'file2.txt'] # pragma: no cover
for filename in mocked_files: # pragma: no cover
    with open(os.path.join(mocked_dir_path, filename), 'w') as f: # pragma: no cover
        f.write('Mock content') # pragma: no cover

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

