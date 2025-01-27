# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_range.py
# GH#43666
sort_order = {8: 2, 6: 0, 4: 8, 2: 10, 0: 12}
values = RangeIndex(0, 10, 2)
result = values.sort_values(key=lambda x: x.map(sort_order))
expected = Index([4, 8, 6, 0, 2], dtype="int64")
tm.assert_index_equal(result, expected, check_exact=True)
