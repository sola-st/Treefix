from pandas import Series, Index # pragma: no cover
import pandas as pd # pragma: no cover
import tempfile # pragma: no cover
import os # pragma: no cover

tmp_path = tempfile.TemporaryDirectory().name # pragma: no cover
setup_path = 'test.h5' # pragma: no cover
path = os.path.join(tmp_path, setup_path) # pragma: no cover
format = 'table' # pragma: no cover
def read_hdf(path, key, errors): return pd.read_hdf(path, key) # pragma: no cover
tm = type('Mock', (object,), {'assert_series_equal': pd.testing.assert_series_equal}) # pragma: no cover

from pandas import Series, Index # pragma: no cover
import pandas as pd # pragma: no cover
import pandas._testing as tm # pragma: no cover
from pathlib import Path # pragma: no cover

tmp_path = Path('./tmp') # pragma: no cover
setup_path = 'test.h5' # pragma: no cover
tmp_path.mkdir(exist_ok=True) # pragma: no cover
path = tmp_path / setup_path # pragma: no cover
format = 'table' # pragma: no cover
def read_hdf(path, key, errors): return pd.read_hdf(path, key) # pragma: no cover
tm.assert_series_equal = pd.testing.assert_series_equal # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_store.py

from l3.Runtime import _l_
data = ["\ud800foo"]
_l_(18676)
ser = Series(data, index=Index(data))
_l_(18677)
path = tmp_path / setup_path
_l_(18678)
# GH 20835
ser.to_hdf(path, "table", format=format, errors="surrogatepass")
_l_(18679)

result = read_hdf(path, "table", errors="surrogatepass")
_l_(18680)
tm.assert_series_equal(result, ser)
_l_(18681)
