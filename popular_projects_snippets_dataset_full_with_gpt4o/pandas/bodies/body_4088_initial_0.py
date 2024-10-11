import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover

float_frame = pd.DataFrame(np.random.randn(25, 5)) # pragma: no cover
int_frame = pd.DataFrame(np.random.randint(0, 100, size=(25, 5))) # pragma: no cover
axis = 0 # pragma: no cover
skipna = True # pragma: no cover
Series = pd.Series # pragma: no cover
tm = type('Mock', (object,), {'assert_series_equal': lambda x, y: print('assert_series_equal called')}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
from l3.Runtime import _l_
frame = float_frame
_l_(21910)
frame.iloc[5:10] = np.nan
_l_(21911)
frame.iloc[15:20, -2:] = np.nan
_l_(21912)
for df in [frame, int_frame]:
    _l_(21916)

    result = df.idxmin(axis=axis, skipna=skipna)
    _l_(21913)
    expected = df.apply(Series.idxmin, axis=axis, skipna=skipna)
    _l_(21914)
    tm.assert_series_equal(result, expected)
    _l_(21915)
