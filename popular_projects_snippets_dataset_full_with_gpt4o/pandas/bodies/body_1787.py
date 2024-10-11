# Extracted from ./data/repos/pandas/pandas/tests/resample/test_datetime_index.py
# GH10914

# use a fixed seed to always have the same uniques
prng = np.random.RandomState(1234)

dr = date_range(start="2015-08-27", periods=n // 10, freq="T").as_unit(unit)
ts = Series(prng.randint(0, n // k, n).astype("int64"), index=prng.choice(dr, n))

left = ts.resample("30T").nunique()
ix = date_range(start=ts.index.min(), end=ts.index.max(), freq="30T").as_unit(unit)

vals = ts.values
bins = np.searchsorted(ix.values, ts.index, side="right")

sorter = np.lexsort((vals, bins))
vals, bins = vals[sorter], bins[sorter]

mask = np.r_[True, vals[1:] != vals[:-1]]
mask |= np.r_[True, bins[1:] != bins[:-1]]

arr = np.bincount(bins[mask] - 1, minlength=len(ix)).astype("int64", copy=False)
right = Series(arr, index=ix)

tm.assert_series_equal(left, right)
