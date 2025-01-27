# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_setops.py
# GH#35876
# values is not an Index -> no name -> retain "a"
values = [pd.Timestamp("2020-01-01"), pd.Timestamp("2020-02-01")]
idx = DatetimeIndex(values, name="a")
res = idx.intersection(values)
tm.assert_index_equal(res, idx)
