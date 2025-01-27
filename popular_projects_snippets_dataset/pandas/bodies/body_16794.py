# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_ordered.py
left = DataFrame(
    {
        "group": list("aaabbb"),
        "key": ["a", "c", "e", "a", "c", "e"],
        "lvalue": [1, 2, 3] * 2,
    }
)

right = DataFrame({"key": ["b", "c", "d"], "rvalue": [1, 2, 3]})

result = merge_ordered(left, right, fill_method="ffill", left_by="group")

expected = DataFrame(
    {
        "group": list("aaaaabbbbb"),
        "key": ["a", "b", "c", "d", "e"] * 2,
        "lvalue": [1, 1, 2, 2, 3] * 2,
        "rvalue": [np.nan, 1, 2, 3, 3] * 2,
    }
)

tm.assert_frame_equal(result, expected)
