import os # pragma: no cover
from typing import List, Tuple # pragma: no cover

def get_crtimes_in_dir(directory: str, raise_on_error: bool = False, as_epoch: bool = False) -> List[Tuple[str, str]]: # pragma: no cover
    try: # pragma: no cover
        return [(filename, os.path.getctime(os.path.join(directory, filename))) for filename in os.listdir(directory)] # pragma: no cover
    except Exception as e: # pragma: no cover
        if raise_on_error: # pragma: no cover
            raise # pragma: no cover
        else: # pragma: no cover
            return [] # pragma: no cover

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

