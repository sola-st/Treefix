# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_join.py

result = left.join(right, how=how, sort=sort, validate="1:1")
tm.assert_frame_equal(result, expected)
