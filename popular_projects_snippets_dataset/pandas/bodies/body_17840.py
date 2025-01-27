# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_frame_equal.py
obj = obj_fixture
msg = f"""{obj}\\.iloc\\[:, 1\\] \\(column name="B"\\) are different

{obj}\\.iloc\\[:, 1\\] \\(column name="B"\\) values are different \\(33\\.33333 %\\)
\\[index\\]: \\[0, 1, 2\\]
\\[left\\]:  \\[4, 5, 6\\]
\\[right\\]: \\[4, 5, 7\\]"""

df1 = DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
df2 = DataFrame({"A": [1, 2, 3], "B": [4, 5, 7]})

with pytest.raises(AssertionError, match=msg):
    tm.assert_frame_equal(df1, df2, by_blocks=by_blocks_fixture, obj=obj_fixture)
