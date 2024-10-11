# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
# test agg using non-callable series attributes
# GH 39116 - expand to apply
s = Series([1, 2, None])

# Calling agg w/ just a string arg same as calling s.arg
result = getattr(s, how)("size")
expected = s.size
assert result == expected

# test when mixed w/ callable reducers
result = getattr(s, how)(["size", "count", "mean"])
expected = Series({"size": 3.0, "count": 2.0, "mean": 1.5})
tm.assert_series_equal(result, expected)
