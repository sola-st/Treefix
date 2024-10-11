# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
c1 = CategoricalDtype(["a", "b"], ordered=ordered)
c2 = CategoricalDtype(["b", "a"], ordered=ordered)
assert hash(c1) == hash(c2)
