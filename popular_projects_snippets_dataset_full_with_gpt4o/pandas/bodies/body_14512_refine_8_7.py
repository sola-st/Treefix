import tempfile as tm # pragma: no cover
import pandas as pd # pragma: no cover
import pytest # pragma: no cover

suffix = '.csv' # pragma: no cover
archive = type('Mock', (object,), {'__enter__': lambda s: s, '__exit__': lambda *args: None}) # pragma: no cover
tm.ensure_clean = lambda suffix: tempfile.NamedTemporaryFile(suffix=suffix, delete=False).__enter__() # pragma: no cover
pytest.raises = lambda exc, match: type('raises', (object,), {'__enter__': lambda s: None, '__exit__': lambda *args: exc() if match in str(args[1]) else None}) # pragma: no cover
pd.read_csv = lambda path: [] if path.name.endswith(suffix) else None # pragma: no cover

import pandas as pd # pragma: no cover
import pytest # pragma: no cover
import tempfile as tm # pragma: no cover
import os # pragma: no cover

suffix = '.csv' # pragma: no cover
archive = type('MockArchive', (object,), {'__enter__': lambda self: self, '__exit__': lambda self, *args: None}) # pragma: no cover
tm.ensure_clean = lambda suffix: tempfile.NamedTemporaryFile(suffix=suffix, delete=False) # pragma: no cover
pytest = type('MockPytest', (object,), {'raises': lambda exc, match: pytest.raises(exc, match=match)}) # pragma: no cover
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
