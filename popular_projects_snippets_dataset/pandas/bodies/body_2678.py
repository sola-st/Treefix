# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_drop_duplicates.py
# GH 30114
df = DataFrame(origin_dict)
expected = DataFrame(output_dict, index=output_index)

if inplace:
    result_df = df.copy()
    result_df.drop_duplicates(ignore_index=ignore_index, inplace=inplace)
else:
    result_df = df.drop_duplicates(ignore_index=ignore_index, inplace=inplace)

tm.assert_frame_equal(result_df, expected)
tm.assert_frame_equal(df, DataFrame(origin_dict))
