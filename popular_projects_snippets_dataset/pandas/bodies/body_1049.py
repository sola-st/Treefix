# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_getitem.py

# GH 6018
# series regression getitem with a multi-index

mi = MultiIndex.from_tuples([(0, 0), (1, 1), (2, 1)], names=["A", "B"])
ser = Series([1, 2, 3], index=mi)
expected.index.name = "A"

result = access_method(ser, level1_value)
tm.assert_series_equal(result, expected)
