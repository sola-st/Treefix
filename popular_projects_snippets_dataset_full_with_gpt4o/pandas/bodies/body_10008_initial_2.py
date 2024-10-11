import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
import pytest # pragma: no cover
from unittest.mock import MagicMock # pragma: no cover

rolling_consistency_cases = (3, 1) # pragma: no cover
f = np.sum # pragma: no cover
no_nans = lambda data: not data.isna().any().any() # pragma: no cover
all_data = pd.DataFrame({'A': [1, 2, np.nan, 4, 5]}) # pragma: no cover
all_na = lambda data: data.isna().all().all() # pragma: no cover
class RequestNode: pass # pragma: no cover
request = type('MockRequest', (object,), {'node': RequestNode()}) # pragma: no cover
request.node.add_marker = MagicMock() # pragma: no cover
pytest.mark = type('MockPytestMark', (object,), {'xfail': lambda reason: reason}) # pragma: no cover
center = False # pragma: no cover
tm = type('MockTM', (object,), {'assert_equal': MagicMock()}) # pragma: no cover

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
