# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_coercion.py
"""test index's coercion triggered by assign key"""
temp = original_series.copy()
# GH#33469 pre-2.0 with int loc_key and temp.index.dtype == np.float64
#  `temp[loc_key] = 5` treated loc_key as positional
temp[loc_key] = 5
exp = pd.Series([1, 2, 3, 4, 5], index=expected_index)
tm.assert_series_equal(temp, exp)
# check dtype explicitly for sure
assert temp.index.dtype == expected_dtype

temp = original_series.copy()
temp.loc[loc_key] = 5
exp = pd.Series([1, 2, 3, 4, 5], index=expected_index)
tm.assert_series_equal(temp, exp)
# check dtype explicitly for sure
assert temp.index.dtype == expected_dtype
