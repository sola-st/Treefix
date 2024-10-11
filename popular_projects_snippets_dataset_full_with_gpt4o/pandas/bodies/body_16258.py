# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH 22477
result = Series(index=[1], dtype=str)
assert np.isnan(result.iloc[0])
