# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
c1 = CategoricalDtype(v1, ordered=False)
c2 = CategoricalDtype(v2, ordered=True)
c3 = CategoricalDtype(v1, ordered=None)
assert c1 is not c2
assert c1 is not c3
