# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# GH#22818; Enforced in 2.0
left = DataFrame({"a": [1, 2, 3], "b": 1, "b_x": 2})
right = DataFrame({"a": [1, 2, 3], "b": 2})

with pytest.raises(MergeError, match="Passing 'suffixes' which cause duplicate"):
    merge(left, right, on="a")

with pytest.raises(MergeError, match="Passing 'suffixes' which cause duplicate"):
    merge(right, left, on="a", suffixes=("_y", "_x"))
