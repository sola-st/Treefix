# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_frame_equal.py
msg = f"""{obj_fixture}\\.index are different

{obj_fixture}\\.index values are different \\(33\\.33333 %\\)
\\[left\\]:  Index\\(\\['a', 'b', 'c'\\], dtype='object'\\)
\\[right\\]: Index\\(\\['a', 'b', 'd'\\], dtype='object'\\)
At positional index 2, first diff: c != d"""

df1 = DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]}, index=["a", "b", "c"])
df2 = DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]}, index=["a", "b", "d"])

with pytest.raises(AssertionError, match=msg):
    tm.assert_frame_equal(df1, df2, check_like=check_like, obj=obj_fixture)
