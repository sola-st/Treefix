# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_join.py

a = DataFrame(np.random.randn(10, 2), columns=["a", "b"], dtype=np.float64)
b = DataFrame(np.random.randn(10, 1), columns=["c"], dtype=np.float32)
joined = a.join(b)
assert joined.dtypes["a"] == "float64"
assert joined.dtypes["b"] == "float64"
assert joined.dtypes["c"] == "float32"

a = np.random.randint(0, 5, 100).astype("int64")
b = np.random.random(100).astype("float64")
c = np.random.random(100).astype("float32")
df = DataFrame({"a": a, "b": b, "c": c})
xpdf = DataFrame({"a": a, "b": b, "c": c})
s = DataFrame(np.random.random(5).astype("float32"), columns=["md"])
rs = df.merge(s, left_on="a", right_index=True)
assert rs.dtypes["a"] == "int64"
assert rs.dtypes["b"] == "float64"
assert rs.dtypes["c"] == "float32"
assert rs.dtypes["md"] == "float32"

xp = xpdf.merge(s, left_on="a", right_index=True)
tm.assert_frame_equal(rs, xp)
