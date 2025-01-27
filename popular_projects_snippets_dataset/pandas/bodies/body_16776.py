# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# GH#44240
left = DataFrame({"a": [1, 2, 3], "b": 1}, dtype=any_numeric_ea_dtype)
right = DataFrame({"a": [1, 2, 3], "c": 2}, dtype=any_numeric_ea_dtype.lower())
result = left.merge(right, how=join_type)
expected = DataFrame(
    {
        "a": Series([1, 2, 3], dtype=any_numeric_ea_dtype),
        "b": Series([1, 1, 1], dtype=any_numeric_ea_dtype),
        "c": Series([2, 2, 2], dtype=any_numeric_ea_dtype.lower()),
    }
)
tm.assert_frame_equal(result, expected)
