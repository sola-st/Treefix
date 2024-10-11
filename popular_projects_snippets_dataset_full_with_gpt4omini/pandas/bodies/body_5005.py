# Extracted from ./data/repos/pandas/pandas/tests/scalar/test_na_scalar.py
if asarray:
    value = np.array([value])
result = NA**value

if asarray:
    result = result[0]
else:
    # this assertion isn't possible for ndarray.
    assert isinstance(result, type(value))
assert result == 1
