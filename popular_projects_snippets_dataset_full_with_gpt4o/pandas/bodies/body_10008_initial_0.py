import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
import pytest # pragma: no cover

rolling_consistency_cases = (3, 1) # pragma: no cover
f = np.sum # pragma: no cover
no_nans = lambda x: not x.isnull().values.any() # pragma: no cover
all_data = pd.DataFrame({'A': [1, 2, 3, np.nan, 5]}) # pragma: no cover
all_na = lambda x: x.isnull().values.all() # pragma: no cover
request = type('Mock', (object,), {'node': type('MockNode', (object,), {'add_marker': lambda self, marker: None})()})() # pragma: no cover
pytest = type('Mock', (object,), {'mark': type('MockMark', (object,), {'xfail': lambda reason: None})()})() # pragma: no cover
center = False # pragma: no cover
tm = type('Mock', (object,), {'assert_equal': lambda a, b: None}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/window/moments/test_moments_consistency_rolling.py
from l3.Runtime import _l_
window, min_periods = rolling_consistency_cases
_l_(21978)

if f is np.sum:
    _l_(21981)

    if not no_nans(all_data) and not (
        all_na(all_data) and not all_data.empty and min_periods > 0
    ):
        _l_(21980)

        request.node.add_marker(
            pytest.mark.xfail(reason="np.sum has different behavior with NaNs")
        )
        _l_(21979)
rolling_f_result = all_data.rolling(
    window=window, min_periods=min_periods, center=center
).sum()
_l_(21982)
rolling_apply_f_result = all_data.rolling(
    window=window, min_periods=min_periods, center=center
).apply(func=f, raw=True)
_l_(21983)
tm.assert_equal(rolling_f_result, rolling_apply_f_result)
_l_(21984)
