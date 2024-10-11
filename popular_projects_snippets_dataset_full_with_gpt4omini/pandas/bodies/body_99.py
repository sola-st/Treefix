# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
class DictWithoutMissing(dict):
    pass

s = Series([1, 2, 3])
dictionary = DictWithoutMissing({3: "three"})
result = s.map(dictionary)
expected = Series([np.nan, np.nan, "three"])
tm.assert_series_equal(result, expected)
