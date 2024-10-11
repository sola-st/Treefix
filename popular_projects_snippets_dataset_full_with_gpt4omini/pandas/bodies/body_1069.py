# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_setitem.py
target.loc[indexers] = value
result = target.loc[indexers]
if expected is None:
    expected = value
compare_fn(result, expected)
