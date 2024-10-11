# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_values.py
# GH 30114
df = DataFrame(original_dict)
expected = DataFrame(sorted_dict, index=output_index)
kwargs = {"ignore_index": ignore_index, "inplace": inplace}

if inplace:
    result_df = df.copy()
    result_df.sort_values("A", ascending=False, **kwargs)
else:
    result_df = df.sort_values("A", ascending=False, **kwargs)

tm.assert_frame_equal(result_df, expected)
tm.assert_frame_equal(df, DataFrame(original_dict))
