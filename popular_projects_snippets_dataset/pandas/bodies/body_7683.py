# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_constructors.py
# GH12258
names = ["A", "B", "C"]
lvl2 = list(range(N))
result = MultiIndex.from_product([[], lvl2, []], names=names)
expected = MultiIndex(levels=[[], lvl2, []], codes=[[], [], []], names=names)
tm.assert_index_equal(result, expected)
