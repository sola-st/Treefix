import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
import pytest # pragma: no cover
import numpy.testing as tm # pragma: no cover

rolling_consistency_cases = (3, 1) # pragma: no cover
f = np.sum # pragma: no cover
no_nans = lambda data: not data.isnull().any() # pragma: no cover
all_data = pd.DataFrame({'a': [1, 2, np.nan, 4], 'b': [np.nan, 2, 3, 4]}) # pragma: no cover
all_na = lambda data: data.isnull().all().all() # pragma: no cover
class MockRequest: node = type('MockNode', (), {})() # pragma: no cover
request = MockRequest() # pragma: no cover
pytest = type('MockPytest', (), {'mark': type('MockMark', (), {' xfail': lambda reason: None})()}) # pragma: no cover
center = False # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/window/moments/test_moments_consistency_rolling.py
from l3.Runtime import _l_
window, min_periods = rolling_consistency_cases
_l_(10592)

if f is np.sum:
    _l_(10595)

    if not no_nans(all_data) and not (
        all_na(all_data) and not all_data.empty and min_periods > 0
    ):
        _l_(10594)

        request.node.add_marker(
            pytest.mark.xfail(reason="np.sum has different behavior with NaNs")
        )
        _l_(10593)
rolling_f_result = all_data.rolling(
    window=window, min_periods=min_periods, center=center
).sum()
_l_(10596)
rolling_apply_f_result = all_data.rolling(
    window=window, min_periods=min_periods, center=center
).apply(func=f, raw=True)
_l_(10597)
tm.assert_equal(rolling_f_result, rolling_apply_f_result)
_l_(10598)
