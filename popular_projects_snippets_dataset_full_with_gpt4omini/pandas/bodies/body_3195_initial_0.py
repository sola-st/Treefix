import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
from pandas import Series, DataFrame # pragma: no cover
import pandas.testing as tm # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_pct_change.py
from l3.Runtime import _l_
s = Series([1.0, 1.5, np.nan, 2.5, 3.0])
_l_(9741)

df = DataFrame({"a": s, "b": s})
_l_(9742)

chg = df.pct_change()
_l_(9743)
expected = Series([np.nan, 0.5, 0.0, 2.5 / 1.5 - 1, 0.2])
_l_(9744)
edf = DataFrame({"a": expected, "b": expected})
_l_(9745)
tm.assert_frame_equal(chg, edf)
_l_(9746)
