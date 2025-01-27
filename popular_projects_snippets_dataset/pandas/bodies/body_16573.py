# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_cross.py
# GH#5401
left = DataFrame({"a": [1, 3]})
right = DataFrame({"a": [3, 4]})
msg = (
    "Can not pass on, right_on, left_on or set right_index=True or "
    "left_index=True"
)
with pytest.raises(MergeError, match=msg):
    left.join(right, how="cross", on="a")
