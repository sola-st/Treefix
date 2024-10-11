# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_sorted.py
frame = multiindex_dataframe_random_data
df = frame.sort_index(level=1).T

# buglet with int typechecking
result = df.iloc[:, : np.int32(3)]
expected = df.reindex(columns=df.columns[:3])
tm.assert_frame_equal(result, expected)
