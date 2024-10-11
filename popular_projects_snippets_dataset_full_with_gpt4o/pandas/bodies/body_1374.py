# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
# GH#44551
df = DataFrame({"A": [1, 2, 3]}, dtype="Int64")

res = df.iloc[:, ::-1]
tm.assert_frame_equal(res, df)

df["B"] = "foo"
res = df.iloc[:, ::-1]
expected = DataFrame({"B": df["B"], "A": df["A"]})
tm.assert_frame_equal(res, expected)
