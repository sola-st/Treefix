# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# GH 15328
df_empty = DataFrame()
df_a = DataFrame({"a": [1, 2]}, index=[0, 1], dtype="int64")
result = merge(df_empty, df_a, left_index=True, right_index=True)
expected = DataFrame({"a": []}, dtype="int64")
tm.assert_frame_equal(result, expected)
