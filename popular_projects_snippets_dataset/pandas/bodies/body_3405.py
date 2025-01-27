# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_pop.py
float_frame.columns.name = "baz"

float_frame.pop("A")
assert "A" not in float_frame

float_frame["foo"] = "bar"
float_frame.pop("foo")
assert "foo" not in float_frame
assert float_frame.columns.name == "baz"

# gh-10912: inplace ops cause caching issue
a = DataFrame([[1, 2, 3], [4, 5, 6]], columns=["A", "B", "C"], index=["X", "Y"])
b = a.pop("B")
b += 1

# original frame
expected = DataFrame([[1, 3], [4, 6]], columns=["A", "C"], index=["X", "Y"])
tm.assert_frame_equal(a, expected)

# result
expected = Series([2, 5], index=["X", "Y"], name="B") + 1
tm.assert_series_equal(b, expected)
