import pandas as pd # pragma: no cover
from pandas import Series, Index # pragma: no cover
import tempfile # pragma: no cover
from pathlib import Path # pragma: no cover
import pandas.testing as tm # pragma: no cover

tmp_path = Path(tempfile.mkdtemp()) # pragma: no cover
setup_path = 'testfile.h5' # pragma: no cover
format = 'table' # pragma: no cover
def read_hdf(path, key, errors='strict'): # pragma: no cover
    return pd.read_hdf(path, key, errors=errors) # pragma: no cover

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
