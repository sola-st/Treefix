import pandas as pd # pragma: no cover
import pytest # pragma: no cover
import tempfile as tm # pragma: no cover
from contextlib import contextmanager # pragma: no cover

suffix = 'test.csv' # pragma: no cover
def archive(path, mode):# pragma: no cover
    class Archive:# pragma: no cover
        def __enter__(self): return path# pragma: no cover
        def __exit__(self, exc_type, exc_val, exc_tb): pass# pragma: no cover
    return Archive() # pragma: no cover

import pandas as pd # pragma: no cover
import pytest # pragma: no cover
import tempfile as tm # pragma: no cover
from contextlib import contextmanager # pragma: no cover

suffix = 'test.csv' # pragma: no cover
@contextmanager# pragma: no cover
def ensure_clean(filename):# pragma: no cover
    tmp_path = os.path.join(os.getcwd(), filename)# pragma: no cover
    try:# pragma: no cover
        yield tmp_path# pragma: no cover
    finally:# pragma: no cover
        if os.path.exists(tmp_path):# pragma: no cover
            os.remove(tmp_path)# pragma: no cover
# pragma: no cover
# Assign the method to the tm module# pragma: no cover
tm.ensure_clean = ensure_clean # pragma: no cover
def archive(path, mode):# pragma: no cover
    class Archive:# pragma: no cover
        def __enter__(self): return path# pragma: no cover
        def __exit__(self, exc_type, exc_val, exc_tb): pass# pragma: no cover
    return Archive() # pragma: no cover

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
