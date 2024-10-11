import pandas as pd # pragma: no cover
import pytest # pragma: no cover
from pandas._testing import ensure_clean # pragma: no cover

suffix = '.csv' # pragma: no cover
filename = 'testfile' # pragma: no cover
class archive: # pragma: no cover
    def __init__(self, path, mode): # pragma: no cover
        self.path = path # pragma: no cover
        self.mode = mode # pragma: no cover
    def __enter__(self): # pragma: no cover
        return self # pragma: no cover
    def __exit__(self, exc_type, exc_val, exc_tb): # pragma: no cover
        with open(self.path, self.mode) as f: # pragma: no cover
            f.write('empty')  # Creating an empty file to trigger ValueError # pragma: no cover
        os.remove(self.path) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/test_compression.py
from l3.Runtime import _l_
with tm.ensure_clean(filename=suffix) as path:
    _l_(21977)

    with archive(path, "w"):
        _l_(21974)

        pass
        _l_(21973)
    with pytest.raises(ValueError, match="Zero files found"):
        _l_(21976)

        pd.read_csv(path)
        _l_(21975)
