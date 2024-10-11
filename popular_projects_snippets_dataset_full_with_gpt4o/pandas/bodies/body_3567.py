# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_index.py
# GH 30114, this is to test ignore_index on MulitIndex of index
mi = MultiIndex.from_tuples([(2, 1), (3, 4)], names=list("AB"))
df = DataFrame(original_dict, index=mi)
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
tm.assert_frame_equal(df, DataFrame(original_dict, index=mi))
