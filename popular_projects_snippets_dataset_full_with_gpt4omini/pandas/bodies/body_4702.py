# Extracted from ./data/repos/pandas/pandas/tests/strings/test_cat.py
# https://github.com/pandas-dev/pandas/issues/18657
box = index_or_series

s = Series(["a", "b", "c", "d"], index=["a", "b", "c", "d"])
t = Series(["D", "A", "E", "B"], index=["d", "a", "e", "b"])
sa, ta = s.align(t, join=join)
# result after manual alignment of inputs
expected = sa.str.cat(ta, na_rep="-")

if box == Index:
    s = Index(s)
    sa = Index(sa)
    expected = Index(expected)

result = s.str.cat(t, join=join, na_rep="-")
assert_series_or_index_equal(result, expected)
