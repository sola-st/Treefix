import pandas as pd # pragma: no cover
import pytest # pragma: no cover
import tempfile as tm # pragma: no cover
from contextlib import contextmanager # pragma: no cover

suffix = 'test.csv' # pragma: no cover
class MockArchive:# pragma: no cover
    def __init__(self, path, mode): pass# pragma: no cover
    def __enter__(self): return self# pragma: no cover
    def __exit__(self, exc_type, exc_value, traceback): pass# pragma: no cover
archive = MockArchive # pragma: no cover
class MockTM:# pragma: no cover
    @contextmanager# pragma: no cover
    def ensure_clean(self, filename):# pragma: no cover
        yield filename# pragma: no cover
        os.remove(filename)# pragma: no cover
tm = MockTM() # pragma: no cover

import pandas as pd # pragma: no cover
import pytest # pragma: no cover
import tempfile as tm # pragma: no cover
from contextlib import contextmanager # pragma: no cover

suffix = 'test.csv' # pragma: no cover
class MockArchive:# pragma: no cover
    def __init__(self, path, mode): self.path = path# pragma: no cover
    def __enter__(self): return self.path# pragma: no cover
    def __exit__(self, exc_type, exc_value, traceback): pass# pragma: no cover
archive = MockArchive # pragma: no cover
class MockTM:# pragma: no cover
    @contextmanager# pragma: no cover
    def ensure_clean(self, filename):# pragma: no cover
        with open(filename, 'w') as f:# pragma: no cover
            f.write('')  # Create an empty file# pragma: no cover
        yield filename# pragma: no cover
        os.remove(filename)  # Remove the file after use# pragma: no cover
tm = MockTM() # pragma: no cover
pd.read_csv = staticmethod(lambda path: pd.DataFrame() if os.path.exists(path) and os.path.getsize(path) > 0 else (_ for _ in ()).throw(ValueError('Zero files found'))) # pragma: no cover

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
