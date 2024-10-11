# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
tdi = pd.timedelta_range(0, periods=5)
ser = pd.Series(tdi)

# Using a single dict argument means we go through replace_list
result = ser.replace({ser[1]: ser[3]})

expected = pd.Series([ser[0], ser[3], ser[2], ser[3], ser[4]])
tm.assert_series_equal(result, expected)
