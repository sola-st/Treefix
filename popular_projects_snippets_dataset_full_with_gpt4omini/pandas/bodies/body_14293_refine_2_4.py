import pandas as pd # pragma: no cover
from pandas import Timestamp # pragma: no cover
from unittest.mock import Mock # pragma: no cover

tm = Mock() # pragma: no cover
tm.makeDataFrame = Mock(return_value=pd.DataFrame({'A': [1, 2], 'B': [3, 4]})) # pragma: no cover
tm.assert_frame_equal = Mock() # pragma: no cover
ensure_clean_store = Mock() # pragma: no cover
setup_path = '/path/to/store' # pragma: no cover
chunksize = 2 # pragma: no cover

import pandas as pd # pragma: no cover
from pandas import Timestamp # pragma: no cover
from unittest.mock import Mock # pragma: no cover

tm = Mock() # pragma: no cover
tm.makeDataFrame = Mock(return_value=pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50], 'C': [100, 200, 300, 400, 500]})) # pragma: no cover
tm.assert_frame_equal = Mock() # pragma: no cover
class MockStore:  # pragma: no cover
    def __enter__(self): # pragma: no cover
        self.store = Mock() # pragma: no cover
        return self.store # pragma: no cover
    def __exit__(self, exc_type, exc_val, exc_tb): # pragma: no cover
        pass # pragma: no cover
ensure_clean_store = Mock(return_value=MockStore()) # pragma: no cover
setup_path = 'test_store.h5' # pragma: no cover
chunksize = 2 # pragma: no cover

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
