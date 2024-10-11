import tempfile as tm # pragma: no cover
import pandas as pd # pragma: no cover
import pytest # pragma: no cover
from contextlib import contextmanager # pragma: no cover

suffix = 'test.csv' # pragma: no cover

import pandas as pd # pragma: no cover
import pytest # pragma: no cover
import tempfile # pragma: no cover
from contextlib import contextmanager # pragma: no cover

suffix = 'test.csv' # pragma: no cover
class MockNamedTemporaryFile:# pragma: no cover
    def __init__(self, delete=True, suffix=''):# pragma: no cover
        self.name = f'tempfile{suffix}'# pragma: no cover
        self.delete = delete# pragma: no cover
    def close(self):# pragma: no cover
        if self.delete:# pragma: no cover
            os.remove(self.name)# pragma: no cover
# pragma: no cover
    def __enter__(self):# pragma: no cover
        return self.name# pragma: no cover
# pragma: no cover
    def __exit__(self, exc_type, exc_val, exc_tb):# pragma: no cover
        self.close() # pragma: no cover
tempfile.NamedTemporaryFile = MockNamedTemporaryFile # pragma: no cover
def ensure_clean(filename): return tempfile.NamedTemporaryFile(delete=False, suffix=f'.{filename}')# pragma: no cover
# pragma: no cover
contextmanager(ensure_clean) # pragma: no cover

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
