# Extracted from ./data/repos/pandas/pandas/tests/window/test_pairwise.py

# DataFrame with another DataFrame, pairwise=False
result = (
    f(pairwise_frames, pairwise_other_frame)
    if pairwise_frames.columns.is_unique
    else None
)
if result is not None:
    with warnings.catch_warnings(record=True):
        warnings.simplefilter("ignore", RuntimeWarning)
        # we can have int and str columns
        expected_index = pairwise_frames.index.union(pairwise_other_frame.index)
        expected_columns = pairwise_frames.columns.union(
            pairwise_other_frame.columns
        )
    tm.assert_index_equal(result.index, expected_index)
    tm.assert_index_equal(result.columns, expected_columns)
else:
    with pytest.raises(ValueError, match="'arg1' columns are not unique"):
        f(pairwise_frames, pairwise_other_frame)
    with pytest.raises(ValueError, match="'arg2' columns are not unique"):
        f(pairwise_other_frame, pairwise_frames)
