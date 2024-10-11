import pandas as pd # pragma: no cover
from pandas import Timestamp # pragma: no cover
import numpy as np # pragma: no cover

tm = type('Mock', (object,), {'makeDataFrame': staticmethod(lambda: pd.DataFrame({'A': [1, 2], 'B': [3, 4]})), 'assert_frame_equal': staticmethod(lambda left, right: pd.testing.assert_frame_equal(left, right))})() # pragma: no cover
Timestamp = pd.Timestamp # pragma: no cover
ensure_clean_store = lambda path, mode: pd.HDFStore(path, mode)  # Mocking the ensure_clean_store behavior # pragma: no cover
setup_path = 'test_store.h5' # pragma: no cover
chunksize = 100 # pragma: no cover

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
