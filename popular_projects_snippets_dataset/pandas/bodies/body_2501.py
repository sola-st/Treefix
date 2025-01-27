# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_getitem.py
# GH#29749
df = DataFrame([[1, 2]], columns=[["a", "b"]])
expected = DataFrame([1], columns=[["a"]])

result = df["a"]
tm.assert_frame_equal(result, expected)

result = df.loc[:, "a"]
tm.assert_frame_equal(result, expected)
