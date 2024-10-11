# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH 29788
ndm = non_dict_mapping_subclass({3: "three"})
result = Series(ndm)
expected = Series(["three"], index=[3])

tm.assert_series_equal(result, expected)
