# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
left = DataFrame({"key": [1], "value": [2]})
right = DataFrame({"key": []})

result = merge(left, right, on="key", how="left")
tm.assert_frame_equal(result, left)

result = merge(right, left, on="key", how="right")
tm.assert_frame_equal(result, left)
