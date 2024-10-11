# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# GH#40073
d1 = DataFrame([("a",)], columns=["id"], dtype=any_string_dtype)
d2 = DataFrame([("b",)], columns=["id"], dtype=any_string_dtype)
result = merge(d1, d2, how=how)
exp_idx = RangeIndex(len(expected_data))
expected = DataFrame(
    expected_data, index=exp_idx, columns=["id"], dtype=any_string_dtype
)
tm.assert_frame_equal(result, expected)
