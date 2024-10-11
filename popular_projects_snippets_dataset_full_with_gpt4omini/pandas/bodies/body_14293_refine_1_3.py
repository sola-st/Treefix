import pandas as pd # pragma: no cover
from pandas import Timestamp # pragma: no cover

tm = type('MockTM', (object,), {'makeDataFrame': lambda: pd.DataFrame({'A': range(5), 'B': range(5, 10)}), 'assert_frame_equal': pd.testing.assert_frame_equal})() # pragma: no cover
setup_path = 'test_store.h5' # pragma: no cover
chunksize = 10 # pragma: no cover

import pandas as pd # pragma: no cover
from pandas import Timestamp # pragma: no cover
import numpy as np # pragma: no cover
import os # pragma: no cover

tm = type('MockTM', (object,), {'makeDataFrame': lambda self: pd.DataFrame(np.random.randn(5, 4), columns=list('ABCD')), 'assert_frame_equal': pd.testing.assert_frame_equal})() # pragma: no cover
setup_path = 'test_store.h5' # pragma: no cover
chunksize = 2 # pragma: no cover
ensure_clean_store = lambda path, mode: pd.HDFStore(path, mode=mode) if not os.path.exists(path) else pd.HDFStore(path, mode='r+') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_append.py
# more chunksize in append tests
from l3.Runtime import _l_
df = tm.makeDataFrame()
_l_(10428)
df["string"] = "foo"
_l_(10429)
df["float322"] = 1.0
_l_(10430)
df["float322"] = df["float322"].astype("float32")
_l_(10431)
df["bool"] = df["float322"] > 0
_l_(10432)
df["time1"] = Timestamp("20130101")
_l_(10433)
df["time2"] = Timestamp("20130102")
_l_(10434)
with ensure_clean_store(setup_path, mode="w") as store:
    _l_(10438)

    store.append("obj", df, chunksize=chunksize)
    _l_(10435)
    result = store.select("obj")
    _l_(10436)
    tm.assert_frame_equal(result, df)
    _l_(10437)
