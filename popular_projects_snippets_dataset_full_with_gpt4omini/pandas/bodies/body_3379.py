# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
df = DataFrame({"a": [True, False, True]})
res = df.replace({"a": {True: "Y", False: "N"}})
expect = DataFrame({"a": ["Y", "N", "Y"]})
tm.assert_frame_equal(res, expect)

df = DataFrame({"a": [0, 1, 0]})
res = df.replace({"a": {0: "Y", 1: "N"}})
expect = DataFrame({"a": ["Y", "N", "Y"]})
tm.assert_frame_equal(res, expect)
