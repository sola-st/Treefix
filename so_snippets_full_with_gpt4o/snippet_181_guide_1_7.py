import os # pragma: no cover
import random # pragma: no cover
from datetime import datetime, timedelta # pragma: no cover

class MockCrTimeModule: # pragma: no cover
    @staticmethod # pragma: no cover
    def get_crtimes_in_dir(directory, raise_on_error=True, as_epoch=False): # pragma: no cover
        mock_data = [] # pragma: no cover
        for i in range(5): # pragma: no cover
            fname = f'file_{i}.txt' # pragma: no cover
            date = datetime.now() - timedelta(days=random.randint(0, 365)) # pragma: no cover
            if as_epoch: # pragma: no cover
                date = int(date.timestamp()) # pragma: no cover
            mock_data.append((fname, date)) # pragma: no cover
        return mock_data # pragma: no cover
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

