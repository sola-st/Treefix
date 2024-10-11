import pandas as pd # pragma: no cover
import pytest # pragma: no cover
import tempfile as tm # pragma: no cover
from contextlib import contextmanager # pragma: no cover

suffix = 'test.csv' # pragma: no cover
def archive(path, mode): return open(path, mode) # pragma: no cover
tm.ensure_clean = lambda filename: filename # pragma: no cover
pytest.raises = lambda exception, match=None: (yield) # pragma: no cover
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
