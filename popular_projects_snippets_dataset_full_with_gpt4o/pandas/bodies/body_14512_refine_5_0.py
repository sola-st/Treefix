import pandas as pd # pragma: no cover
import pytest # pragma: no cover
import tempfile as tm # pragma: no cover

suffix = '.csv' # pragma: no cover
archive = type('MockArchive', (object,), {'__enter__': lambda self: self, '__exit__': lambda self, *args: None}) # pragma: no cover
tm.ensure_clean = lambda suffix: tempfile.NamedTemporaryFile(suffix=suffix, delete=False) # pragma: no cover
pytest.raises = lambda exc, match: pytest.raises(exc, match=match) # pragma: no cover
pd.read_csv = pd.read_csv # pragma: no cover

import pandas as pd # pragma: no cover
import pytest # pragma: no cover
import tempfile as tm # pragma: no cover
import os # pragma: no cover

suffix = '.zip' # pragma: no cover
archive = type('MockArchive', (object,), {'__init__': lambda self, path, mode: None, '__enter__': lambda self: self, '__exit__': lambda self, *args: None}) # pragma: no cover
class ensure_clean:# pragma: no cover
    def __init__(self, suffix):# pragma: no cover
        self.suffix = suffix# pragma: no cover
        self.tempfile = None# pragma: no cover
    def __enter__(self):# pragma: no cover
        self.tempfile = tm.NamedTemporaryFile(suffix=self.suffix, delete=False)# pragma: no cover
        return self.tempfile.name# pragma: no cover
    def __exit__(self, exc_type, exc_value, traceback):# pragma: no cover
        if self.tempfile:# pragma: no cover
            os.remove(self.tempfile.name)# pragma: no cover
tm.ensure_clean = ensure_clean # pragma: no cover
pytest.raises = lambda exc, match: pytest.raises(exc, match=match) # pragma: no cover
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
