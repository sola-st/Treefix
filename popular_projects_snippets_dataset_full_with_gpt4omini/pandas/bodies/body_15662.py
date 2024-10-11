# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_interpolate.py
# https://github.com/pandas-dev/pandas/pull/34746
s = Series([1, 2, 3])

msg = f"`limit_direction` must be '{expected}' for method `{method}`"
with pytest.raises(ValueError, match=msg):
    s.interpolate(method=method, limit_direction=limit_direction)
