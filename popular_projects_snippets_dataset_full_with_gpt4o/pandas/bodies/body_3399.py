# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
# GH#40371
obj = frame_or_series(data)
expected = frame_or_series(expected)
result = obj.replace(box(to_replace), value)
tm.assert_equal(result, expected)
