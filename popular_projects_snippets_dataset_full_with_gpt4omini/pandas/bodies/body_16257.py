# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
result = Series(index=["b", "a", "c"])
assert result.index.tolist() == ["b", "a", "c"]
