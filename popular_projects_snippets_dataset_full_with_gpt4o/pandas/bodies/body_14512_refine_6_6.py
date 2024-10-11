import tempfile # pragma: no cover
import zipfile # pragma: no cover
import pytest # pragma: no cover
import pandas as pd # pragma: no cover

tm = type('Mock', (object,), {'ensure_clean': lambda suffix: tempfile.NamedTemporaryFile(suffix=suffix)}) # pragma: no cover
suffix = '.zip' # pragma: no cover
archive = zipfile.ZipFile # pragma: no cover
pytest = type('pytest', (object,), {'raises': pytest.raises}) # pragma: no cover
pd = pd # pragma: no cover

import pandas as pd # pragma: no cover
import pytest # pragma: no cover
import tempfile as tm # pragma: no cover
import contextlib # pragma: no cover

suffix = '.zip' # pragma: no cover
archive = lambda path, mode: contextlib.nullcontext() # pragma: no cover
tm.ensure_clean = lambda suffix: tempfile.NamedTemporaryFile(suffix=suffix, delete=False) # pragma: no cover
pytest.raises = lambda exc, match: contextlib.nullcontext() if exc is ValueError else pytest.raises(exc) # pragma: no cover

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
