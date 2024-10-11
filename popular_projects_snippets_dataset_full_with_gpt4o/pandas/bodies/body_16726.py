# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# GH#40073
d1 = DataFrame([(1,)], columns=["id"], dtype=any_numeric_ea_dtype)
d2 = DataFrame([(2,)], columns=["id"], dtype=any_numeric_ea_dtype)
result = merge(d1, d2, how=how)
exp_index = RangeIndex(len(expected_data))
expected = DataFrame(
    expected_data, index=exp_index, columns=["id"], dtype=any_numeric_ea_dtype
)
tm.assert_frame_equal(result, expected)
