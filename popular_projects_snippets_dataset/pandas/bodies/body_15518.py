# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_drop_duplicates.py
tc2 = cat_series

expected = Series([False, False, False, False, True, True, False])

result = tc2.duplicated()
tm.assert_series_equal(result, expected)

result = tc2.drop_duplicates()
tm.assert_series_equal(result, tc2[~expected])

sc = tc2.copy()
return_value = sc.drop_duplicates(inplace=True)
assert return_value is None
tm.assert_series_equal(sc, tc2[~expected])
