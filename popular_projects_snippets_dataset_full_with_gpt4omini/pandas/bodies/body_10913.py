# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_indexing.py
g = column_group_df.groupby(column_group_df.iloc[1], axis=1)
result = g._positional_selector[1:-1]
expected = column_group_df.iloc[:, [1, 3]]

tm.assert_frame_equal(result, expected)
