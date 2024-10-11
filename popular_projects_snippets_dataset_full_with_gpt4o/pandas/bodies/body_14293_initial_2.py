import pandas as pd # pragma: no cover
from pandas._testing import makeDataFrame # pragma: no cover
from pandas import Timestamp # pragma: no cover
import pandas.testing as tm # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_append.py
# more chunksize in append tests
from l3.Runtime import _l_
df = tm.makeDataFrame()
_l_(21263)
df["string"] = "foo"
_l_(21264)
df["float322"] = 1.0
_l_(21265)
df["float322"] = df["float322"].astype("float32")
_l_(21266)
df["bool"] = df["float322"] > 0
_l_(21267)
df["time1"] = Timestamp("20130101")
_l_(21268)
df["time2"] = Timestamp("20130102")
_l_(21269)
with ensure_clean_store(setup_path, mode="w") as store:
    _l_(21273)

    store.append("obj", df, chunksize=chunksize)
    _l_(21270)
    result = store.select("obj")
    _l_(21271)
    tm.assert_frame_equal(result, df)
    _l_(21272)
