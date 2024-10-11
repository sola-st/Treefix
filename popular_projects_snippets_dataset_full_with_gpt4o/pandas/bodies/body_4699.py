# Extracted from ./data/repos/pandas/pandas/tests/strings/test_cat.py
box = index_or_series

s = Index(["a", "a", "b", "a"], dtype=dtype_caller)
s = s if box == Index else Series(s, index=s)
t = Index(["b", "a", "b", "c"], dtype=dtype_target)

expected = Index(["ab", "aa", "bb", "ac"])
expected = expected if box == Index else Series(expected, index=s)

# Series/Index with unaligned Index -> t.values
result = s.str.cat(t.values, sep=sep)
assert_series_or_index_equal(result, expected)

# Series/Index with Series having matching Index
t = Series(t.values, index=s)
result = s.str.cat(t, sep=sep)
assert_series_or_index_equal(result, expected)

# Series/Index with Series.values
result = s.str.cat(t.values, sep=sep)
assert_series_or_index_equal(result, expected)

# Series/Index with Series having different Index
t = Series(t.values, index=t.values)
expected = Index(["aa", "aa", "aa", "bb", "bb"])
expected = expected if box == Index else Series(expected, index=expected.str[:1])

result = s.str.cat(t, sep=sep)
assert_series_or_index_equal(result, expected)
