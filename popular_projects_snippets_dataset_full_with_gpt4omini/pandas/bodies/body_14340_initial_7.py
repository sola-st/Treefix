import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover
import tempfile # pragma: no cover

Series = pd.Series # pragma: no cover
Index = pd.Index # pragma: no cover
tmp_path = tempfile.TemporaryDirectory() # pragma: no cover
setup_path = 'test.h5' # pragma: no cover
read_hdf = pd.read_hdf # pragma: no cover
tm = type('Mock', (object,), {'assert_series_equal': lambda self, left, right: pd.testing.assert_series_equal(left, right)}) # pragma: no cover

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
