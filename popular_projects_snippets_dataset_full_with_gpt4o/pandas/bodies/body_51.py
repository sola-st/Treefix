# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
with np.errstate(all="ignore"):
    tm.assert_series_equal(datetime_series.apply(np.sqrt), np.sqrt(datetime_series))

    # element-wise apply
    tm.assert_series_equal(datetime_series.apply(math.exp), np.exp(datetime_series))

# empty series
s = Series(dtype=object, name="foo", index=Index([], name="bar"))
rs = s.apply(lambda x: x)
tm.assert_series_equal(s, rs)

# check all metadata (GH 9322)
assert s is not rs
assert s.index is rs.index
assert s.dtype == rs.dtype
assert s.name == rs.name

# index but no data
s = Series(index=[1, 2, 3], dtype=np.float64)
rs = s.apply(lambda x: x)
tm.assert_series_equal(s, rs)
