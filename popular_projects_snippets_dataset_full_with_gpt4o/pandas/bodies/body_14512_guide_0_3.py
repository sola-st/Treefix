import pandas as pd # pragma: no cover
import pytest # pragma: no cover
from pandas._testing import ensure_clean as tm # pragma: no cover

filename = '' # pragma: no cover
suffix = '.csv' # pragma: no cover
archive = type('Mock', (object,), {'__enter__': lambda self: None, '__exit__': lambda self, exc_type, exc_val, exc_tb: None}) # pragma: no cover

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
