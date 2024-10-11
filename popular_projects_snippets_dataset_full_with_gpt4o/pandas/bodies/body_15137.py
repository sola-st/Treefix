# Extracted from ./data/repos/pandas/pandas/tests/series/test_npfuncs.py
# GH#21614
N = 1000
arr = np.random.randn(N)
ser = Series(arr)
assert np.ptp(ser) == np.ptp(arr)
