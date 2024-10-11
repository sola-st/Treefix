# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
df = DataFrame({"a": [metachar, "else"]})
result = df.replace({"a": {metachar: "paren"}})
expected = DataFrame({"a": ["paren", "else"]})
tm.assert_frame_equal(result, expected)
