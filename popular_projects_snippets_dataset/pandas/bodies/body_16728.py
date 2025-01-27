# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# GH#40073
df1 = DataFrame({"A": [True, False], "B": [1, 5]})
df2 = DataFrame({"A": [False, True], "C": [3, 4]})
result = merge(df1, df2, how=how)
expected = DataFrame(expected_data, columns=["A", "B", "C"])
tm.assert_frame_equal(result, expected)
