# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
c1 = CategoricalDtype(["a", "b"], ordered=True)
c2 = CategoricalDtype(["b", "a"], ordered=True)
assert c1 is not c2
