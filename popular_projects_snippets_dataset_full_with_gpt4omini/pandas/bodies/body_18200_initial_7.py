import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover
import pandas.testing as tm # pragma: no cover
from pandas import Series # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
# integer div, but deal with the 0's (GH#9144)
from l3.Runtime import _l_
df = pd.DataFrame({"first": [3, 4, 5, 8], "second": [0, 0, 0, 3]})
_l_(10708)
result = df / df
_l_(10709)

first = Series([1.0, 1.0, 1.0, 1.0])
_l_(10710)
second = Series([np.nan, np.nan, np.nan, 1])
_l_(10711)
expected = pd.DataFrame({"first": first, "second": second})
_l_(10712)
tm.assert_frame_equal(result, expected)
_l_(10713)
