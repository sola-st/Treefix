# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval.py
expected = self.create_index(closed=closed)

result = expected.copy()
assert result.equals(expected)

result = expected.copy(deep=True)
assert result.equals(expected)
assert result.left is not expected.left
