# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
# GH26632
df = DataFrame(["a"])
result = df.replace({"a": replacer, "b": replacer})
expected = DataFrame([replacer])
tm.assert_frame_equal(result, expected)
