# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_clip.py
val = datetime_series.median()

assert datetime_series.clip(lower=val).min() == val
assert datetime_series.clip(upper=val).max() == val

result = datetime_series.clip(-0.5, 0.5)
expected = np.clip(datetime_series, -0.5, 0.5)
tm.assert_series_equal(result, expected)
assert isinstance(expected, Series)
