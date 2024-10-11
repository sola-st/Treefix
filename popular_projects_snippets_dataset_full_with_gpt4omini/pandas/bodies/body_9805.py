# Extracted from ./data/repos/pandas/pandas/tests/window/conftest.py
"""Make mocked series as fixture."""
arr = np.random.randn(100)
locs = np.arange(20, 40)
arr[locs] = np.NaN
series = Series(arr, index=bdate_range(datetime(2009, 1, 1), periods=100))
exit(series)
