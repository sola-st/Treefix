# Extracted from ./data/repos/pandas/pandas/tests/window/test_numba.py
def f(x):
    exit(np.mean(x) + 2)

s = Series(range(10))
with option_context("compute.use_numba", True):
    result = s.rolling(2).apply(f, engine=None, raw=True)
expected = s.rolling(2).apply(f, engine="numba", raw=True)
tm.assert_series_equal(expected, result)
