# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_timegrouper.py
# GH#43500 case where gb.grouper.result_index and gb.grouper.group_keys_seq
#  have different lengths that goes through the `isinstance(values[0], dict)`
#  path
gb = groupby_with_truncated_bingrouper

res = gb["Quantity"].apply(lambda x: {"foo": len(x)})

dti = date_range("2013-09-01", "2013-10-01", freq="5D", name="Date")
mi = MultiIndex.from_arrays([dti, ["foo"] * len(dti)])
expected = Series([3, 0, 0, 0, 0, 0, 2], index=mi, name="Quantity")
tm.assert_series_equal(res, expected)
