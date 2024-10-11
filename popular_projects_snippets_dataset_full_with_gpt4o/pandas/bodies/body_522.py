# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
c1 = CategoricalDtype([1, 2, 3])
c2 = CategoricalDtype([1.0, 2.0, 3.0])
assert c1 is not c2
assert c1 != c2
