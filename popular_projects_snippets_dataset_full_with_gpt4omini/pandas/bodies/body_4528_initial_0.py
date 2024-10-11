import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover
from pandas import Series, DataFrame # pragma: no cover
import pandas.testing as tm # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
from l3.Runtime import _l_
rng1 = pd.period_range("1/1/1999", "1/1/2012", freq="M")
_l_(10281)
s1 = Series(np.random.randn(len(rng1)), rng1)
_l_(10282)

rng2 = pd.period_range("1/1/1980", "12/1/2001", freq="M")
_l_(10283)
s2 = Series(np.random.randn(len(rng2)), rng2)
_l_(10284)
df = DataFrame({"s1": s1, "s2": s2})
_l_(10285)

exp = pd.period_range("1/1/1980", "1/1/2012", freq="M")
_l_(10286)
tm.assert_index_equal(df.index, exp)
_l_(10287)
