# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# name
s1 = Series([1, 2, 3], index=["a", "b", "c"], name="x")

# no name
s2 = Series([1, 2, 3], index=["a", "b", "c"])

other_index = Index(["a", "b"])

df1 = DataFrame(s1, index=other_index)
exp1 = DataFrame(s1.reindex(other_index))
assert df1.columns[0] == "x"
tm.assert_frame_equal(df1, exp1)

df2 = DataFrame(s2, index=other_index)
exp2 = DataFrame(s2.reindex(other_index))
assert df2.columns[0] == 0
tm.assert_index_equal(df2.index, other_index)
tm.assert_frame_equal(df2, exp2)
