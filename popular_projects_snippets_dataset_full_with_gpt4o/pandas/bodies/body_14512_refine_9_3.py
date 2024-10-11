import tempfile # pragma: no cover
import pandas as pd # pragma: no cover
import pytest # pragma: no cover

tm = type('Mock', (object,), {'ensure_clean': tempfile.NamedTemporaryFile}) # pragma: no cover
suffix = '.csv' # pragma: no cover
archive = type('MockArchive', (object,), {'__enter__': lambda self: None, '__exit__': lambda self, exc_type, exc_value, traceback: None}) # pragma: no cover
pytest = type('Mock', (object,), {'raises': pytest.raises}) # pragma: no cover
pd = pd # pragma: no cover

import pandas as pd # pragma: no cover
import pytest # pragma: no cover
import tempfile # pragma: no cover
import os # pragma: no cover

suffix = '.csv' # pragma: no cover
archive = type('MockArchive', (object,), {'__enter__': lambda self: open(self.path, 'w'), '__exit__': lambda self, exc_type, exc_value, traceback: os.remove(self.path)}) # pragma: no cover
tm = type('MockTM', (object,), {'ensure_clean': lambda suffix: contextlib.nullcontext(tempfile.NamedTemporaryFile(suffix=suffix, delete=False))}) # pragma: no cover
pytest = type('MockPytest', (object,), {'raises': pytest.raises}) # pragma: no cover
pd = pd # pragma: no cover

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
