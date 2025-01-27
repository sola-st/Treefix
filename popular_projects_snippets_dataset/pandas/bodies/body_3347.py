# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
# from GH 3064
df = DataFrame({"zero": {"a": 0.0, "b": 1}, "one": {"a": 2.0, "b": 0}})
result = df.replace(0, {"zero": 0.5, "one": 1.0})
expected = DataFrame({"zero": {"a": 0.5, "b": 1}, "one": {"a": 2.0, "b": 1.0}})
tm.assert_frame_equal(result, expected)

result = df.replace(0, df.mean())
tm.assert_frame_equal(result, expected)

# series to series/dict
df = DataFrame({"zero": {"a": 0.0, "b": 1}, "one": {"a": 2.0, "b": 0}})
s = Series({"zero": 0.0, "one": 2.0})
result = df.replace(s, {"zero": 0.5, "one": 1.0})
expected = DataFrame({"zero": {"a": 0.5, "b": 1}, "one": {"a": 1.0, "b": 0.0}})
tm.assert_frame_equal(result, expected)

result = df.replace(s, df.mean())
tm.assert_frame_equal(result, expected)
