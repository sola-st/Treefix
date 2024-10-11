import pandas as pd # pragma: no cover
from pandas import Series, Index, read_hdf # pragma: no cover
import tempfile # pragma: no cover
import os # pragma: no cover
import pandas.testing as tm # pragma: no cover

tmp_path = tempfile.mkdtemp() # pragma: no cover
setup_path = 'test_data.h5' # pragma: no cover
format = 'table' # pragma: no cover
data = ['\ud800foo'] # pragma: no cover
ser = Series(data, index=Index(data)) # pragma: no cover
os.makedirs(tmp_path, exist_ok=True) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_store.py

from l3.Runtime import _l_
data = ["\ud800foo"]
_l_(6730)
ser = Series(data, index=Index(data))
_l_(6731)
path = tmp_path / setup_path
_l_(6732)
# GH 20835
ser.to_hdf(path, "table", format=format, errors="surrogatepass")
_l_(6733)

result = read_hdf(path, "table", errors="surrogatepass")
_l_(6734)
tm.assert_series_equal(result, ser)
_l_(6735)
