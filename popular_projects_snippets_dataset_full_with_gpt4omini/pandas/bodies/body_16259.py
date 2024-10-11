# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH 22477
result = Series(item, index=[1], dtype=str)
assert result.iloc[0] == str(item)
