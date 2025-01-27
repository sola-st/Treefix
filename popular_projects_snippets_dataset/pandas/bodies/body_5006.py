# Extracted from ./data/repos/pandas/pandas/tests/scalar/test_na_scalar.py
if asarray:
    value = np.array([value])
result = value**NA

if asarray:
    result = result[0]
elif not isinstance(value, (np.float_, np.bool_, np.int_)):
    # this assertion isn't possible with asarray=True
    assert isinstance(result, type(value))

assert result == value
