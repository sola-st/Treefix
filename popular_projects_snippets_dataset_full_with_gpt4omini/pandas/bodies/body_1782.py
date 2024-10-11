# Extracted from ./data/repos/pandas/pandas/tests/resample/test_datetime_index.py

# GH 6418
# resample with bfill / limit / reindex consistency

i30 = date_range("2002-02-02", periods=4, freq="30T").as_unit(unit)
s = Series(np.arange(4.0), index=i30)
s[2] = np.NaN

# Upsample by factor 3 with reindex() and resample() methods:
i10 = date_range(i30[0], i30[-1], freq="10T").as_unit(unit)

s10 = s.reindex(index=i10, method="bfill")
s10_2 = s.reindex(index=i10, method="bfill", limit=2)
rl = s.reindex_like(s10, method="bfill", limit=2)
r10_2 = s.resample("10Min").bfill(limit=2)
r10 = s.resample("10Min").bfill()

# s10_2, r10, r10_2, rl should all be equal
tm.assert_series_equal(s10_2, r10)
tm.assert_series_equal(s10_2, r10_2)
tm.assert_series_equal(s10_2, rl)
