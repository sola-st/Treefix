# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
# GH 27660 keep behaviour consistent for simple dictionary and
# nested dictionary replacement
df = DataFrame({"a": list(range(1, 5))})

result = df.replace({"a": dict(zip(range(1, 5), range(2, 6)))})
expected = df.replace(dict(zip(range(1, 5), range(2, 6))))
tm.assert_frame_equal(result, expected)
