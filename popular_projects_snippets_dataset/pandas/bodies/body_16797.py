# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_ordered.py
# GH 38167
left = DataFrame([["g", "h", 1], ["g", "h", 3]], columns=list("GHE"))
right = DataFrame([[2, 1]], columns=list("ET"))
msg = r"\{'h'\} not found in left columns"
with pytest.raises(KeyError, match=msg):
    merge_ordered(left, right, on="E", left_by=["G", "h"])
