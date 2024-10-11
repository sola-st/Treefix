# Extracted from ./data/repos/pandas/pandas/tests/series/test_missing.py
# NumPy limitation =(
# https://github.com/pandas-dev/pandas/commit/9030dc021f07c76809848925cb34828f6c8484f3
np.random.seed(12345)
selector = -0.5 <= datetime_series <= 0.5
expected = (datetime_series >= -0.5) & (datetime_series <= 0.5)
tm.assert_series_equal(selector, expected)
