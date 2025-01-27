# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_rank.py
from scipy.stats import rankdata

xs = np.random.randn(9)
xs = np.concatenate([xs[i:] for i in range(0, 9, 2)])  # add duplicates
np.random.shuffle(xs)

index = [chr(ord("a") + i) for i in range(len(xs))]
vals = op(xs, value)
ts = Series(vals, index=index)
result = ts.rank(method=method)
sprank = rankdata(vals, method if method != "first" else "ordinal")
expected = Series(sprank, index=index).astype("float64")
tm.assert_series_equal(result, expected)
