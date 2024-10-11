# Extracted from ./data/repos/pandas/pandas/tests/window/test_pairwise.py

# DataFrame with itself, pairwise=True
# note that we may construct the 1st level of the MI
# in a non-monotonic way, so compare accordingly
result = f(pairwise_frames)
tm.assert_index_equal(
    result.index.levels[0], pairwise_frames.index, check_names=False
)
tm.assert_index_equal(
    safe_sort(result.index.levels[1]),
    safe_sort(pairwise_frames.columns.unique()),
)
tm.assert_index_equal(result.columns, pairwise_frames.columns)
expected = f(pairwise_target_frame)
# since we have sorted the results
# we can only compare non-nans
result = result.dropna().values
expected = expected.dropna().values

tm.assert_numpy_array_equal(result, expected, check_dtype=False)
