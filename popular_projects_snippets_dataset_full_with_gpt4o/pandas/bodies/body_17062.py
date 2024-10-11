# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_index.py
# is_series and ignore_index
s1 = Series([1, 2, 3], name="x")
s2 = Series([4, 5, 6], name="y")
res = concat([s1, s2], axis=1, ignore_index=True)
assert isinstance(res.columns, pd.RangeIndex)
exp = DataFrame([[1, 4], [2, 5], [3, 6]])
# use check_index_type=True to check the result have
# RangeIndex (default index)
tm.assert_frame_equal(res, exp, check_index_type=True, check_column_type=True)

# is_series and all inputs have no names
s1 = Series([1, 2, 3])
s2 = Series([4, 5, 6])
res = concat([s1, s2], axis=1, ignore_index=False)
assert isinstance(res.columns, pd.RangeIndex)
exp = DataFrame([[1, 4], [2, 5], [3, 6]])
exp.columns = pd.RangeIndex(2)
tm.assert_frame_equal(res, exp, check_index_type=True, check_column_type=True)

# is_dataframe and ignore_index
df1 = DataFrame({"A": [1, 2], "B": [5, 6]})
df2 = DataFrame({"A": [3, 4], "B": [7, 8]})

res = concat([df1, df2], axis=0, ignore_index=True)
exp = DataFrame([[1, 5], [2, 6], [3, 7], [4, 8]], columns=["A", "B"])
tm.assert_frame_equal(res, exp, check_index_type=True, check_column_type=True)

res = concat([df1, df2], axis=1, ignore_index=True)
exp = DataFrame([[1, 5, 3, 7], [2, 6, 4, 8]])
tm.assert_frame_equal(res, exp, check_index_type=True, check_column_type=True)
