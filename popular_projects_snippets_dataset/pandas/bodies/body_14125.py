# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
s = Series(["foo", np.nan, -1.23, 4.56])
result = s.to_string()
expected = "0     foo\n" + "1     NaN\n" + "2   -1.23\n" + "3    4.56"
assert result == expected

# but don't count NAs as floats
s = Series(["foo", np.nan, "bar", "baz"])
result = s.to_string()
expected = "0    foo\n" + "1    NaN\n" + "2    bar\n" + "3    baz"
assert result == expected

s = Series(["foo", 5, "bar", "baz"])
result = s.to_string()
expected = "0    foo\n" + "1      5\n" + "2    bar\n" + "3    baz"
assert result == expected
