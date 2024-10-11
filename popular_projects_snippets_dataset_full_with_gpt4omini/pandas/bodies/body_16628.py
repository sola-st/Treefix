# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_asof.py
msg = r"Incompatible merge dtype, .*, both sides must have numeric dtype"

left = pd.DataFrame({"left_val": [1, 5, 10], "a": ["a", "b", "c"]})
right = pd.DataFrame({"right_val": [1, 2, 3, 6, 7], "a": [1, 2, 3, 6, 7]})

with pytest.raises(MergeError, match=msg):
    merge_asof(left, right, on="a")
