# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_frame_equal.py
msg = f"""{obj_fixture}\\.columns are different

{obj_fixture}\\.columns values are different \\(50\\.0 %\\)
\\[left\\]:  Index\\(\\['A', 'B'\\], dtype='object'\\)
\\[right\\]: Index\\(\\['A', 'b'\\], dtype='object'\\)"""

df1 = DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]}, index=["a", "b", "c"])
df2 = DataFrame({"A": [1, 2, 3], "b": [4, 5, 6]}, index=["a", "b", "c"])

with pytest.raises(AssertionError, match=msg):
    tm.assert_frame_equal(df1, df2, check_like=check_like, obj=obj_fixture)
