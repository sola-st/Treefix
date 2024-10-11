# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_indexing.py
# GH#8667

from pandas._libs.index import _SIZE_CUTOFF

ns = _SIZE_CUTOFF + np.array([-100, 100], dtype=np.int64)
key = time(15, 11, 30)
start = key.hour * 3600 + key.minute * 60 + key.second
step = 24 * 3600

for n in ns:
    idx = date_range("2014-11-26", periods=n, freq="S")
    ts = pd.Series(np.random.randn(n), index=idx)
    locs = np.arange(start, n, step, dtype=np.intp)

    result = ts.index.get_loc(key)
    tm.assert_numpy_array_equal(result, locs)
    tm.assert_series_equal(ts[key], ts.iloc[locs])

    left, right = ts.copy(), ts.copy()
    left[key] *= -10
    right.iloc[locs] *= -10
    tm.assert_series_equal(left, right)
