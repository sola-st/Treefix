# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_frozen.py
result = container.union((1, 2, 3))
expected = FrozenList(lst + [1, 2, 3])
self.check_result(result, expected)
