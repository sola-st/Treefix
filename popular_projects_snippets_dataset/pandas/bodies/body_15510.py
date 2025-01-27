# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_drop_duplicates.py
tc = Series([True, False, True, False])

tm.assert_series_equal(tc.duplicated(keep=keep), expected)
tm.assert_series_equal(tc.drop_duplicates(keep=keep), tc[~expected])
sc = tc.copy()
return_value = sc.drop_duplicates(keep=keep, inplace=True)
tm.assert_series_equal(sc, tc[~expected])
assert return_value is None
