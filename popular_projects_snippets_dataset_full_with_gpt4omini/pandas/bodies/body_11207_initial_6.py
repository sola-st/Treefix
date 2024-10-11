import pandas as pd # pragma: no cover
import pandas._testing as tm # pragma: no cover

DataFrame = pd.DataFrame # pragma: no cover
func = 'sum' # pragma: no cover
Index = pd.Index # pragma: no cover
tm = type('Mock', (object,), {'assert_frame_equal': staticmethod(lambda x, y: None)})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
# GH#37493
from l3.Runtime import _l_
val = 922337203685477580
_l_(10133)
df = DataFrame({"a": 1, "b": [val]})
_l_(10134)
result = getattr(df.groupby("a"), func)() - val
_l_(10135)
expected = DataFrame({"b": [0]}, index=Index([1], name="a"))
_l_(10136)
if func in ["cumsum", "cumprod"]:
    _l_(10138)

    expected = expected.reset_index(drop=True)
    _l_(10137)
tm.assert_frame_equal(result, expected)
_l_(10139)
