# Extracted from ./data/repos/pandas/pandas/tests/window/test_pairwise.py

# DataFrame with another DataFrame, pairwise=True
result = f(pairwise_frames, pairwise_other_frame)
tm.assert_index_equal(
    result.index.levels[0], pairwise_frames.index, check_names=False
)
tm.assert_index_equal(
    safe_sort(result.index.levels[1]),
    safe_sort(pairwise_other_frame.columns.unique()),
)
expected = f(pairwise_target_frame, pairwise_other_frame)
# since we have sorted the results
# we can only compare non-nans
result = result.dropna().values
expected = expected.dropna().values

tm.assert_numpy_array_equal(result, expected, check_dtype=False)
