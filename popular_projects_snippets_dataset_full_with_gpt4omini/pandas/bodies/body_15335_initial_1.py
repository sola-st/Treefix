import pandas as pd # pragma: no cover
from pandas import date_range, Series # pragma: no cover
from pandas import IntervalIndex # pragma: no cover
import numpy as np # pragma: no cover
import pandas.testing as tm # pragma: no cover
from typing import Callable # pragma: no cover
from functools import partial # pragma: no cover

date_range = pd.date_range # pragma: no cover
pd = type('MockPandas', (object,), {'date_range': date_range, 'IntervalIndex': pd.IntervalIndex, 'Series': Series})() # pragma: no cover
Series = pd.Series # pragma: no cover
box = lambda x: [x] # pragma: no cover
tm = type('MockTesting', (object,), {'assert_series_equal': lambda a, b: None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
# GH#33404 fall back to positional since ints are unambiguous
from l3.Runtime import _l_
dti = date_range("2000-01-03", periods=3)._with_freq(None)
_l_(10485)
ii = pd.IntervalIndex.from_breaks(dti)
_l_(10486)
ser = Series(range(len(ii)), index=ii)
_l_(10487)

expected = ser.iloc[:1]
_l_(10488)
key = box([0])
_l_(10489)
result = ser[key]
_l_(10490)
tm.assert_series_equal(result, expected)
_l_(10491)
