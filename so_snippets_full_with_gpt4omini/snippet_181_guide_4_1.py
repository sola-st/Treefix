import os # pragma: no cover
from typing import List, Tuple # pragma: no cover

def get_crtimes_in_dir(directory: str, raise_on_error: bool = True, as_epoch: bool = False) -> List[Tuple[str, str]]: # pragma: no cover
    # Simulated function to return file names and their creation dates # pragma: no cover
    return [('file1.txt', '2023-10-01 10:00:00'), ('file2.txt', '2023-10-02 15:30:00')] # pragma: no cover

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

