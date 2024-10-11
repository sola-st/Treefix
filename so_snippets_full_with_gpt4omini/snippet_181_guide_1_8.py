from datetime import datetime # pragma: no cover
from typing import List, Tuple # pragma: no cover

def get_crtimes_in_dir(directory: str, raise_on_error: bool = False, as_epoch: bool = False) -> List[Tuple[str, str]]: # pragma: no cover
    # Assuming the function will return a list of tuples with file names and fake creation times # pragma: no cover
    return [(f'file_{i}.txt', datetime.now().strftime('%Y-%m-%d %H:%M:%S')) for i in range(3)] # pragma: no cover

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

