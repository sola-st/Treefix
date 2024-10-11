# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
result = frame.replace(to_replace, value)
tm.assert_frame_equal(result, expected)
