# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_getitem.py
# GH#46185
df = DataFrame([[1, 2]], columns=Index(["A", "B"], dtype="string"))
result = df.A
expected = df["A"]
tm.assert_series_equal(result, expected)
