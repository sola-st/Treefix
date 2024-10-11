# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_duplicated.py
# GH 25184

df = DataFrame(columns=["a", "b"])
dupes = df.duplicated("a")

result = df[dupes]
expected = df.copy()
tm.assert_frame_equal(result, expected)
