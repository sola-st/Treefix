# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# GH: 16228
left = DataFrame({"a": [1, 2], "b": [3, 4]})
right = DataFrame({"a": [1, 1], "c": [5, 6]})
msg = (
    r'Can only pass argument "on" OR "left_index" '
    r'and "right_index", not a combination of both\.'
)
with pytest.raises(MergeError, match=msg):
    getattr(pd, func)(left, right, on="a", **kwargs)
