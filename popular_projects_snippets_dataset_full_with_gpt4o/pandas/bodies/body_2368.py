# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_xs.py
# GH#19056
df = DataFrame([[1, 2, 3]], columns=Index(["a", "b", "c"]))
result = df.xs("a", axis=1, drop_level=False)
expected = DataFrame({"a": [1]})
tm.assert_frame_equal(result, expected)
