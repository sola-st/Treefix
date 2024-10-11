# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
# GH#48231
df = DataFrame({"a": [1, val]})
result = df.replace(val, None)
expected = DataFrame({"a": [1, None]}, dtype=object)
tm.assert_frame_equal(result, expected)

df = DataFrame({"a": [1, val]})
result = df.replace({val: None})
tm.assert_frame_equal(result, expected)
