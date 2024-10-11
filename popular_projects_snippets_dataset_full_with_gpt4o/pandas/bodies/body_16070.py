# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_str_accessor.py
# GH#9068
methods = ["strip", "rstrip", "lstrip"]
ser = Series([" jack", "jill ", " jesse ", "frank"])
for method in methods:
    expected = Series([getattr(str, method)(x) for x in ser.values])
    tm.assert_series_equal(getattr(Series.str, method)(ser.str), expected)

# str accessor only valid with string values
ser = Series(range(5))
with pytest.raises(AttributeError, match="only use .str accessor"):
    ser.str.repeat(2)
