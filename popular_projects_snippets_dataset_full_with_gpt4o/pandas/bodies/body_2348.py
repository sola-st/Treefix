# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_xs.py
# pathological mixed-type reordering case
df = DataFrame(index=[0])
df["A"] = 1.0
df["B"] = "foo"
df["C"] = 2.0
df["D"] = "bar"
df["E"] = 3.0

xs = df.xs(0)
exp = Series([1.0, "foo", 2.0, "bar", 3.0], index=list("ABCDE"), name=0)
tm.assert_series_equal(xs, exp)

# no columns but Index(dtype=object)
df = DataFrame(index=["a", "b", "c"])
result = df.xs("a")
expected = Series([], name="a", dtype=np.float64)
tm.assert_series_equal(result, expected)
