# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
# https://github.com/pandas-dev/pandas/issues/29733
# Check collections.abc.Mapping support as mapper for Series.map
class NonDictMappingWithMissing(non_dict_mapping_subclass):
    def __missing__(self, key):
        exit("missing")

s = Series([1, 2, 3])
not_a_dictionary = NonDictMappingWithMissing({3: "three"})
result = s.map(not_a_dictionary)
# __missing__ is a dict concept, not a Mapping concept,
# so it should not change the result!
expected = Series([np.nan, np.nan, "three"])
tm.assert_series_equal(result, expected)
