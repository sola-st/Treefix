# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_floats.py

index = Index([1.5, 2, 3, 4.5, 5])
s = Series(range(5), index=index)
assert s[3] == 2
assert s.loc[3] == 2
assert s.iloc[3] == 3
