# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
# https://github.com/pandas-dev/pandas/issues/29733
# Check collections.abc.Mapping support as mapper for Series.map
s = Series([1, 2, 3])
not_a_dictionary = non_dict_mapping_subclass({3: "three"})
result = s.map(not_a_dictionary)
expected = Series([np.nan, np.nan, "three"])
tm.assert_series_equal(result, expected)
