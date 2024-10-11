import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
import pandas.testing as tm # pragma: no cover

float_frame = pd.DataFrame(np.random.rand(20, 5)) # pragma: no cover
int_frame = pd.DataFrame(np.random.randint(0, 100, size=(20, 5))) # pragma: no cover
axis = 0 # pragma: no cover
skipna = True # pragma: no cover
Series = pd.Series # pragma: no cover
tm = type('Mock', (object,), {'assert_series_equal': staticmethod(lambda a, b: None)}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
from l3.Runtime import _l_
frame = float_frame
_l_(10520)
frame.iloc[5:10] = np.nan
_l_(10521)
frame.iloc[15:20, -2:] = np.nan
_l_(10522)
for df in [frame, int_frame]:
    _l_(10526)

    result = df.idxmin(axis=axis, skipna=skipna)
    _l_(10523)
    expected = df.apply(Series.idxmin, axis=axis, skipna=skipna)
    _l_(10524)
    tm.assert_series_equal(result, expected)
    _l_(10525)
