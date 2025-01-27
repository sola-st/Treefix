# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_setops.py
first = index[5:20]
first.name = "name"
result = first.difference(first, sort)

assert len(result) == 0
assert result.name == first.name
