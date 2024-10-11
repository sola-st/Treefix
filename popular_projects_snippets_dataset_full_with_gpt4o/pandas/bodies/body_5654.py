# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
from scipy.stats import rankdata

arr = np.array(arr)

mask = ~np.isfinite(arr)
arr = arr.copy()
result = libalgos.rank_1d(arr)
arr[mask] = np.inf
exp = rankdata(arr)
exp[mask] = np.nan
tm.assert_almost_equal(result, exp)
