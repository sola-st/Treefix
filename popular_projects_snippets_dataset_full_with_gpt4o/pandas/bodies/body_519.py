# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
categories = ["a", "b"]
c1 = CategoricalDtype(categories, ordered=True)
c2 = CategoricalDtype(categories, ordered=False)
c3 = CategoricalDtype(categories, ordered=None)
assert c1 is not c2
assert c1 is not c3
