# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_frozen.py
result = FrozenList([1, 2, 3, 2]).difference([2])
expected = FrozenList([1, 3])
self.check_result(result, expected)
