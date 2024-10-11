# Extracted from ./data/repos/pandas/pandas/tests/scalar/test_na_scalar.py
if asarray:
    value = np.array([value])
result = value**NA

if asarray:
    result = result[0]

assert pd.isna(result)
