# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_value_counts.py
# GH 41334
# 3-way compare with :meth:`~DataFrame.value_counts`
# Tests with nulls from frame/methods/test_value_counts.py
result_frame = names_with_nulls_df.value_counts(dropna=dropna, normalize=normalize)
expected = Series(
    data=expected_data,
    index=expected_index,
)
if normalize:
    expected /= float(len(expected_data))

tm.assert_series_equal(result_frame, expected)

result_frame_groupby = names_with_nulls_df.groupby("key").value_counts(
    dropna=dropna, normalize=normalize
)

tm.assert_series_equal(result_frame_groupby, expected)
