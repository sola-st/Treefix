# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
data = {}
data["A"] = {"foo": 1, "bar": 2, "baz": 3}
data["B"] = Series([4, 3, 2, 1], index=["bar", "qux", "baz", "foo"])

result = DataFrame(data)
assert result.index.is_monotonic_increasing

# ordering ambiguous, raise exception
with pytest.raises(ValueError, match="ambiguous ordering"):
    DataFrame({"A": ["a", "b"], "B": {"a": "a", "b": "b"}})

# this is OK though
result = DataFrame({"A": ["a", "b"], "B": Series(["a", "b"], index=["a", "b"])})
expected = DataFrame({"A": ["a", "b"], "B": ["a", "b"]}, index=["a", "b"])
tm.assert_frame_equal(result, expected)
