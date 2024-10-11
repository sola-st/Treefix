# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_index.py
# GH 30114
original_index = [2, 5, 3]
df = DataFrame(original_dict, index=original_index)
expected_df = DataFrame(sorted_dict, index=output_index)
kwargs = {
    "ascending": ascending,
    "ignore_index": ignore_index,
    "inplace": inplace,
}

if inplace:
    result_df = df.copy()
    result_df.sort_index(**kwargs)
else:
    result_df = df.sort_index(**kwargs)

tm.assert_frame_equal(result_df, expected_df)
tm.assert_frame_equal(df, DataFrame(original_dict, index=original_index))
