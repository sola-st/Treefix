# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_frozen.py
result = container[1:2]
expected = lst[1:2]
self.check_result(result, expected)
