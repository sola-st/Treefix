# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_loc.py
df = frame_random_data_integer_multi_index
result = df.loc[1]
expected = df[-3:]
expected.index = expected.index.droplevel(0)
tm.assert_frame_equal(result, expected)
