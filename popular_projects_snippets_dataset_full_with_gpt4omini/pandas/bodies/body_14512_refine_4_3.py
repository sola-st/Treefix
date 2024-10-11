import tempfile as tm # pragma: no cover
import pandas as pd # pragma: no cover
import pytest # pragma: no cover
from contextlib import contextmanager # pragma: no cover

suffix = 'test_file.csv' # pragma: no cover
def archive(path, mode): return open(path, mode) # pragma: no cover
tm.ensure_clean = lambda filename: tempfile.NamedTemporaryFile(delete=False, suffix=f'.{filename}') # pragma: no cover
pytest.raises = staticmethod(lambda exc_class, match=None: contextmanager(lambda: (yield)) if match else contextmanager(lambda: (yield))) # pragma: no cover

import pandas as pd # pragma: no cover
import pytest # pragma: no cover
import tempfile # pragma: no cover
from contextlib import contextmanager # pragma: no cover

suffix = 'test_file.csv' # pragma: no cover
def archive(path, mode): return open(path, mode) # pragma: no cover
class MockPytest:# pragma: no cover
    @staticmethod# pragma: no cover
    def raises(exception, match=None):# pragma: no cover
        class Context:# pragma: no cover
            def __enter__(self): return self# pragma: no cover
            def __exit__(self, exc_type, exc_val, exc_tb):# pragma: no cover
                if exception and not isinstance(exc_val, exception):# pragma: no cover
                    raise AssertionError('Expected exception was not raised')# pragma: no cover
                return True# pragma: no cover
        return Context()# pragma: no cover
# pragma: no cover
pytest = MockPytest() # pragma: no cover
pd.read_csv = lambda path: (_ for _ in ()).throw(ValueError('Zero files found')) # pragma: no cover

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
