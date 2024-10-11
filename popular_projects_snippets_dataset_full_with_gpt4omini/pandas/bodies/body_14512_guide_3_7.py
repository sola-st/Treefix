import pandas as pd # pragma: no cover
import pytest # pragma: no cover
import tempfile # pragma: no cover
from zipfile import ZipFile # pragma: no cover

suffix = '.zip' # pragma: no cover
def archive(path, mode): return ZipFile(path, mode) # pragma: no cover
tm = type('MockTempfileManager', (object,), {'ensure_clean': staticmethod(lambda filename: 'mock_path' + filename)})() # pragma: no cover

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
