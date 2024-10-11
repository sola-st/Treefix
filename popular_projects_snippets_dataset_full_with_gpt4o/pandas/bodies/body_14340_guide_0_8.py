import pandas as pd # pragma: no cover
from pandas import Series, Index # pragma: no cover
import tempfile # pragma: no cover
import os # pragma: no cover

setup_path = 'test_hdf5.h5' # pragma: no cover
format = 'table' # pragma: no cover
type('Mock', (object,), dict(to_hdf=pd.Series.to_hdf, read_hdf=pd.read_hdf)) # pragma: no cover
def ensure_dir(path): # pragma: no cover
    if not os.path.exists(path): os.makedirs(path) # pragma: no cover

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
