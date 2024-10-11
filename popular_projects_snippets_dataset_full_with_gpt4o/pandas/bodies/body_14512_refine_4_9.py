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
import zipfile # pragma: no cover
import os # pragma: no cover

suffix = '.zip' # pragma: no cover
archive = zipfile.ZipFile # pragma: no cover
class TM: # pragma: no cover
    @staticmethod # pragma: no cover
    def ensure_clean(suffix): # pragma: no cover
        temp_file = tempfile.NamedTemporaryFile(suffix=suffix, delete=False) # pragma: no cover
        temp_file.close() # pragma: no cover
        return temp_file.name # pragma: no cover
tm = TM() # pragma: no cover

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
