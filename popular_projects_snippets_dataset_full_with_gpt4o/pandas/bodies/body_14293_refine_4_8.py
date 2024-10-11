import pandas as pd # pragma: no cover
from pandas import Timestamp # pragma: no cover

setup_path = 'path/to/store.h5' # pragma: no cover
chunksize = 1000 # pragma: no cover

import pandas as pd # pragma: no cover
from pandas import Timestamp # pragma: no cover
from pandas.testing import assert_frame_equal # pragma: no cover
from pandas._testing import makeDataFrame # pragma: no cover

tm = type('Mock', (object,), {'makeDataFrame': makeDataFrame, 'assert_frame_equal': assert_frame_equal}) # pragma: no cover
class ensure_clean_store:# pragma: no cover
    def __init__(self, path, mode):# pragma: no cover
        self.path = path# pragma: no cover
        self.mode = mode# pragma: no cover
    def __enter__(self):# pragma: no cover
        self.store = pd.HDFStore(self.path, self.mode)# pragma: no cover
        return self.store# pragma: no cover
    def __exit__(self, exc_type, exc_val, exc_tb):# pragma: no cover
        self.store.close() # pragma: no cover
setup_path = 'test_store.h5' # pragma: no cover
chunksize = 5 # pragma: no cover

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
