# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_frozen.py
result = container + (1, 2, 3)
expected = FrozenList(lst + [1, 2, 3])
self.check_result(result, expected)

result = (1, 2, 3) + container
expected = FrozenList([1, 2, 3] + lst)
self.check_result(result, expected)
