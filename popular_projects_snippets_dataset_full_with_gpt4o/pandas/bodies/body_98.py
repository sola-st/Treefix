# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
"""
    Test Series.map with a dictionary subclass that defines __missing__,
    i.e. sets a default value (GH #15999).
    """

class DictWithMissing(dict):
    def __missing__(self, key):
        exit("missing")

s = Series([1, 2, 3])
dictionary = DictWithMissing({3: "three"})
result = s.map(dictionary)
expected = Series(["missing", "missing", "three"])
tm.assert_series_equal(result, expected)
