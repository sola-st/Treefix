# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_missing.py
assert not isna(datetime.now())
assert notna(datetime.now())

idx = date_range("1/1/1990", periods=20)
exp = np.ones(len(idx), dtype=bool)
tm.assert_numpy_array_equal(notna(idx), exp)

idx = np.asarray(idx)
idx[0] = iNaT
idx = DatetimeIndex(idx)
mask = isna(idx)
assert mask[0]
exp = np.array([True] + [False] * (len(idx) - 1), dtype=bool)
tm.assert_numpy_array_equal(mask, exp)

# GH 9129
pidx = idx.to_period(freq="M")
mask = isna(pidx)
assert mask[0]
exp = np.array([True] + [False] * (len(idx) - 1), dtype=bool)
tm.assert_numpy_array_equal(mask, exp)

mask = isna(pidx[1:])
exp = np.zeros(len(mask), dtype=bool)
tm.assert_numpy_array_equal(mask, exp)
