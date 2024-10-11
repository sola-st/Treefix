# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py

# GH8626

# dict creation
df = DataFrame({"A": list("abc")}, dtype="category")
expected = Series(list("abc"), dtype="category", name="A")
tm.assert_series_equal(df["A"], expected)

# to_frame
s = Series(list("abc"), dtype="category")
result = s.to_frame()
expected = Series(list("abc"), dtype="category", name=0)
tm.assert_series_equal(result[0], expected)
result = s.to_frame(name="foo")
expected = Series(list("abc"), dtype="category", name="foo")
tm.assert_series_equal(result["foo"], expected)

# list-like creation
df = DataFrame(list("abc"), dtype="category")
expected = Series(list("abc"), dtype="category", name=0)
tm.assert_series_equal(df[0], expected)
