import pandas as pd # pragma: no cover
import pytest # pragma: no cover
from unittest import mock # pragma: no cover
import tempfile as tm # pragma: no cover

suffix = '.csv' # pragma: no cover
archive = lambda *args, **kwargs: mock.MagicMock() # pragma: no cover
tm.ensure_clean = mock.MagicMock() # pragma: no cover
path = 'mock_path.csv' # pragma: no cover

import pandas as pd # pragma: no cover
import pytest # pragma: no cover
import tempfile as tm # pragma: no cover
import os # pragma: no cover

suffix = '.zip' # pragma: no cover
class MockArchive: # pragma: no cover
    def __init__(self, path, mode): # pragma: no cover
        self.path = path # pragma: no cover
    def __enter__(self): # pragma: no cover
        return self # pragma: no cover
    def __exit__(self, exc_type, exc_val, exc_tb): # pragma: no cover
        if os.path.exists(self.path): # pragma: no cover
            os.remove(self.path) # pragma: no cover
archive = MockArchive # pragma: no cover
tm.ensure_clean = lambda suffix: tempfile.NamedTemporaryFile(suffix=suffix, delete=False) # pragma: no cover

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
