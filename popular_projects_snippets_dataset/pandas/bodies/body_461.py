# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
rng = pd.Index(range(3))
dtype = CategoricalDtype(categories=rng, ordered=False)
result = repr(dtype)

expected = "CategoricalDtype(categories=range(0, 3), ordered=False)"
assert result == expected
