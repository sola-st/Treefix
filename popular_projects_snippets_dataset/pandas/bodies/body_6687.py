# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_frozen.py
result = container.difference([2])
expected = FrozenList([1, 3, 4, 5])
self.check_result(result, expected)
