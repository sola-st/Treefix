# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5137497/find-the-current-directory-and-files-directory
from l3.Runtime import _l_
try:
    import pathlib
    _l_(1521)

except ImportError:
    pass
filepath = pathlib.Path(__file__).resolve().parent
_l_(1522)

