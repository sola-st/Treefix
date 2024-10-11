import pandas as pd # pragma: no cover
import pytest # pragma: no cover
from contextlib import contextmanager # pragma: no cover
import os # pragma: no cover

import pandas as pd # pragma: no cover
import pytest # pragma: no cover
import tempfile as tm # pragma: no cover
import os # pragma: no cover

class MockArchive:# pragma: no cover
    def __init__(self, path, mode):# pragma: no cover
        self.path = path# pragma: no cover
        self.mode = mode# pragma: no cover
    def __enter__(self): return self.path# pragma: no cover
    def __exit__(self, exc_type, exc_val, exc_tb): pass # pragma: no cover
suffix = 'test_file.csv' # pragma: no cover
def archive(path, mode): return MockArchive(path, mode) # pragma: no cover
tm.ensure_clean = lambda filename: tempfile.NamedTemporaryFile(delete=False, suffix=filename).name # pragma: no cover

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
