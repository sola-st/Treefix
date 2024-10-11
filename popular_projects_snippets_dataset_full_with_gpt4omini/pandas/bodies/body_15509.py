# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_drop_duplicates.py
tc = Series([1, 0, 3, 5, 3, 0, 4], dtype=np.dtype(any_numpy_dtype))

if tc.dtype == "bool":
    pytest.skip("tested separately in test_drop_duplicates_bool")

tm.assert_series_equal(tc.duplicated(keep=keep), expected)
tm.assert_series_equal(tc.drop_duplicates(keep=keep), tc[~expected])
sc = tc.copy()
return_value = sc.drop_duplicates(keep=keep, inplace=True)
assert return_value is None
tm.assert_series_equal(sc, tc[~expected])
