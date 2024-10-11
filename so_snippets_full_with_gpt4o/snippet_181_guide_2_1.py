import sys # pragma: no cover

class MockCrTimeModule: # pragma: no cover
    @staticmethod # pragma: no cover
    def get_crtimes_in_dir(directory, raise_on_error=True, as_epoch=False): # pragma: no cover
        return [ # pragma: no cover
            ('file1.txt', '2023-01-01 12:00:00'), # pragma: no cover
            ('file2.txt', '2023-02-01 12:00:00'), # pragma: no cover
            ('file3.txt', '2023-03-01 12:00:00') # pragma: no cover
        ] # pragma: no cover
sys.modules['crtime'] = MockCrTimeModule # pragma: no cover

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

