# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
# GH 25259
dtype = any_string_dtype
df = DataFrame({"first": ["abc", "bca", "cab"]}, dtype=dtype)
expected = DataFrame({"first": [".bc", "bc.", "c.b"]}, dtype=dtype)
result = df.replace({"a": "."}, regex=True)
tm.assert_frame_equal(result, expected)
