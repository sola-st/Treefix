# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_categorical.py
# list of labels
result = df.loc[["c", "a"]]
expected = df.iloc[[4, 0, 1, 5]]
tm.assert_frame_equal(result, expected, check_index_type=True)
