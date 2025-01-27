# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
# GH 27338
result = CategoricalDtype(["a"]).update_dtype(Categorical(["b"], ordered=True))
expected = CategoricalDtype(["b"], ordered=True)
assert result == expected
