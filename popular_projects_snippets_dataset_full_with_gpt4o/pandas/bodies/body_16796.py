# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_ordered.py
# GH 38166
left = DataFrame([["g", "h", 1], ["g", "h", 3]], columns=list("GHE"))
right = DataFrame([[2, 1]], columns=list("ET"))
result = merge_ordered(left, right, on="E", left_by=["G", "H"])
expected = DataFrame(
    {"G": ["g"] * 3, "H": ["h"] * 3, "E": [1, 2, 3], "T": [np.nan, 1.0, np.nan]}
)

tm.assert_frame_equal(result, expected)
