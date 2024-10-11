import tempfile as tm # pragma: no cover
import pandas as pd # pragma: no cover
import pytest # pragma: no cover
from unittest.mock import Mock # pragma: no cover

suffix = '.csv' # pragma: no cover
archive = Mock() # pragma: no cover
pytest.raises = Mock(side_effect=ValueError('Zero files found')) # pragma: no cover
pd.read_csv = Mock(side_effect=ValueError('Zero files found')) # pragma: no cover

import pandas as pd # pragma: no cover
import pytest # pragma: no cover
import tempfile as tm # pragma: no cover
import os # pragma: no cover
import zipfile # pragma: no cover

suffix = '.zip' # pragma: no cover
archive = zipfile.ZipFile # pragma: no cover
class EnsureClean: # pragma: no cover
    def __init__(self, suffix): # pragma: no cover
        self.suffix = suffix # pragma: no cover
        self.file = None # pragma: no cover
    def __enter__(self): # pragma: no cover
        self.file = tempfile.NamedTemporaryFile(suffix=self.suffix, delete=False) # pragma: no cover
        return self.file.name # pragma: no cover
    def __exit__(self, exc_type, exc_value, traceback): # pragma: no cover
        if self.file: # pragma: no cover
            os.remove(self.file.name) # pragma: no cover
tm.ensure_clean = EnsureClean # pragma: no cover
pytest.raises = pytest.raises # pragma: no cover
pd.read_csv = pd.read_csv # pragma: no cover

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
