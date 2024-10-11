import pandas as pd # pragma: no cover
import pytest # pragma: no cover
import tempfile # pragma: no cover
from contextlib import contextmanager # pragma: no cover

suffix = '.csv' # pragma: no cover
class MockTempfileManager: # pragma: no cover
    @staticmethod # pragma: no cover
    def ensure_clean(filename): return 'mocked_clean_file.csv' # pragma: no cover
tm = MockTempfileManager() # pragma: no cover
class MockArchive: # pragma: no cover
    def __init__(self, path, mode): pass # pragma: no cover
def archive(path, mode): return MockArchive(path, mode) # pragma: no cover
pd.read_csv = lambda path: (_ for _ in ()).throw(ValueError('Zero files found')) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/test_compression.py
from l3.Runtime import _l_
with tm.ensure_clean(filename=suffix) as path:
    _l_(10603)

    with archive(path, "w"):
        _l_(10600)

        pass
        _l_(10599)
    with pytest.raises(ValueError, match="Zero files found"):
        _l_(10602)

        pd.read_csv(path)
        _l_(10601)
