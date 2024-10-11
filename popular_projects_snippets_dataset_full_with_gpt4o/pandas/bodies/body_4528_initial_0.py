import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover
from pandas import Series, DataFrame # pragma: no cover
import pandas._testing as tm # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
from l3.Runtime import _l_
rng1 = pd.period_range("1/1/1999", "1/1/2012", freq="M")
_l_(21325)
s1 = Series(np.random.randn(len(rng1)), rng1)
_l_(21326)

rng2 = pd.period_range("1/1/1980", "12/1/2001", freq="M")
_l_(21327)
s2 = Series(np.random.randn(len(rng2)), rng2)
_l_(21328)
df = DataFrame({"s1": s1, "s2": s2})
_l_(21329)

exp = pd.period_range("1/1/1980", "1/1/2012", freq="M")
_l_(21330)
tm.assert_index_equal(df.index, exp)
_l_(21331)
