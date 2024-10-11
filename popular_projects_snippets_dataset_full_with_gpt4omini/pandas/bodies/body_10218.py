# Extracted from ./data/repos/pandas/pandas/tests/window/test_pairwise.py

# DataFrame with a Series
result = f(pairwise_frames, Series([1, 1, 3, 8]))
tm.assert_index_equal(result.index, pairwise_frames.index)
tm.assert_index_equal(result.columns, pairwise_frames.columns)
expected = f(pairwise_target_frame, Series([1, 1, 3, 8]))
# since we have sorted the results
# we can only compare non-nans
result = result.dropna().values
expected = expected.dropna().values
tm.assert_numpy_array_equal(result, expected, check_dtype=False)

result = f(Series([1, 1, 3, 8]), pairwise_frames)
tm.assert_index_equal(result.index, pairwise_frames.index)
tm.assert_index_equal(result.columns, pairwise_frames.columns)
expected = f(Series([1, 1, 3, 8]), pairwise_target_frame)
# since we have sorted the results
# we can only compare non-nans
result = result.dropna().values
expected = expected.dropna().values
tm.assert_numpy_array_equal(result, expected, check_dtype=False)
