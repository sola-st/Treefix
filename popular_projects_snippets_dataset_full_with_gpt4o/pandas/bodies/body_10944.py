# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_value_counts.py
# 3-way compare with :meth:`~DataFrame.value_counts`
# Tests from frame/methods/test_value_counts.py
result_frame = animals_df.value_counts(
    sort=sort, ascending=ascending, normalize=normalize
)
expected = Series(
    data=expected_data,
    index=MultiIndex.from_arrays(
        expected_index, names=["key", "num_legs", "num_wings"]
    ),
)
tm.assert_series_equal(result_frame, expected)

result_frame_groupby = animals_df.groupby("key").value_counts(
    sort=sort, ascending=ascending, normalize=normalize
)

tm.assert_series_equal(result_frame_groupby, expected)
