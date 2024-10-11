import pandas as pd # pragma: no cover
import pytest # pragma: no cover
import tempfile # pragma: no cover
import os # pragma: no cover

suffix = '.csv' # pragma: no cover
filename = '' # pragma: no cover
class MockArchive: # pragma: no cover
    def __init__(self, path, mode): # pragma: no cover
        self.path = path # pragma: no cover
        self.mode = mode # pragma: no cover
    def __enter__(self): # pragma: no cover
        open(self.path, 'w').close()  # Create an empty file # pragma: no cover
        return self # pragma: no cover
    def __exit__(self, exc_type, exc_val, exc_tb): # pragma: no cover
        # Ensure the file stays empty # pragma: no cover
        with open(self.path, 'w') as f: # pragma: no cover
            f.truncate(0) # pragma: no cover
archive = MockArchive # pragma: no cover
class MockTestManagement: # pragma: no cover
    @staticmethod # pragma: no cover
    def ensure_clean(filename=None): # pragma: no cover
        with tempfile.NamedTemporaryFile(delete=False, suffix=filename) as tmp_file: # pragma: no cover
            yield tmp_file.name # pragma: no cover
tm = MockTestManagement # pragma: no cover

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
