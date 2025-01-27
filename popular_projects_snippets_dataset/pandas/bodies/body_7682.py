# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_constructors.py
names = ["A", "B"]
result = MultiIndex.from_product([first, second], names=names)
expected = MultiIndex(levels=[first, second], codes=[[], []], names=names)
tm.assert_index_equal(result, expected)
