# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_records.py
# GH#8626

# dict creation
df = DataFrame({"A": list("abc")}, dtype="category")
expected = Series(list("abc"), dtype="category", name="A")
tm.assert_series_equal(df["A"], expected)

# list-like creation
df = DataFrame(list("abc"), dtype="category")
expected = Series(list("abc"), dtype="category", name=0)
tm.assert_series_equal(df[0], expected)

# to record array
# this coerces
result = df.to_records()
expected = np.rec.array(
    [(0, "a"), (1, "b"), (2, "c")], dtype=[("index", "=i8"), ("0", "O")]
)
tm.assert_almost_equal(result, expected)
