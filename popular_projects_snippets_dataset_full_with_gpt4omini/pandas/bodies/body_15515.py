# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_drop_duplicates.py
tc1 = cat_series_unused_category

expected = Series([False, False, True, False])

result = tc1.duplicated(keep="last")
tm.assert_series_equal(result, expected)

result = tc1.drop_duplicates(keep="last")
tm.assert_series_equal(result, tc1[~expected])

sc = tc1.copy()
return_value = sc.drop_duplicates(keep="last", inplace=True)
assert return_value is None
tm.assert_series_equal(sc, tc1[~expected])
