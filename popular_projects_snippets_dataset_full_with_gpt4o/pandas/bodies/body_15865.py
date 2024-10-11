# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
# GH 26988
dti = pd.date_range("2016-01-01", periods=3, tz="US/Pacific")
s = pd.Series(dti)
c = s.astype("category")

expected = c.copy()
expected = expected.cat.add_categories("foo")
expected[2] = "foo"
expected = expected.cat.remove_unused_categories()
assert c[2] != "foo"

result = c.replace(c[2], "foo")
tm.assert_series_equal(expected, result)
assert c[2] != "foo"  # ensure non-inplace call does not alter original

return_value = c.replace(c[2], "foo", inplace=True)
assert return_value is None
tm.assert_series_equal(expected, c)

first_value = c[0]
return_value = c.replace(c[1], c[0], inplace=True)
assert return_value is None
assert c[0] == c[1] == first_value  # test replacing with existing value
