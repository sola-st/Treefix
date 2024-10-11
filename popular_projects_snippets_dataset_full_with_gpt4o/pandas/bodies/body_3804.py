# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_join.py
# GH 46622
# Two column join, dups in both, but jointly no dups
left = DataFrame(
    {
        "a": ["a", "a", "b", "b"],
        "b": [0, 1, 0, 1],
        "c": ["cat", "dog", "weasel", "horse"],
    },
    index=range(4),
).set_index(["a", "b"])

right = DataFrame(
    {
        "a": ["a", "a", "b"],
        "b": [0, 1, 0],
        "d": ["meow", "bark", "um... weasel noise?"],
    },
    index=range(3),
).set_index(["a", "b"])

expected_multi = DataFrame(
    {
        "a": ["a", "a", "b"],
        "b": [0, 1, 0],
        "c": ["cat", "dog", "weasel"],
        "d": ["meow", "bark", "um... weasel noise?"],
    },
    index=range(3),
).set_index(["a", "b"])

# Jointly no dups allowed by one_to_one constraint
result = left.join(right, how="inner", validate="1:1")
tm.assert_frame_equal(result, expected_multi)
