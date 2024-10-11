import pandas as pd # pragma: no cover
import pandas.testing as tm # pragma: no cover
import tempfile # pragma: no cover
from pathlib import Path # pragma: no cover

Series = pd.Series # pragma: no cover
Index = pd.Index # pragma: no cover
tmp_path = Path(tempfile.mkdtemp()) # pragma: no cover
setup_path = Path('hdf5_test.h5') # pragma: no cover
read_hdf = pd.read_hdf # pragma: no cover
MockTM = type('MockTM', (object,), {'assert_series_equal': tm.assert_series_equal}) # pragma: no cover
tm = MockTM # pragma: no cover

import pandas as pd # pragma: no cover
import pandas.testing as tm # pragma: no cover
import tempfile # pragma: no cover
from pathlib import Path # pragma: no cover

Series = pd.Series # pragma: no cover
Index = pd.Index # pragma: no cover
tmp_path = Path(tempfile.mkdtemp()) # pragma: no cover
setup_path = Path('hdf5_test.h5') # pragma: no cover
path = tmp_path / setup_path # pragma: no cover
format = 'table' # pragma: no cover
read_hdf = pd.read_hdf # pragma: no cover
MockTM = type('MockTM', (object,), {'assert_series_equal': tm.assert_series_equal}) # pragma: no cover
tm = MockTM # pragma: no cover

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
