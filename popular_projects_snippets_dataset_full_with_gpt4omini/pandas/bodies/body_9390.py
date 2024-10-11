# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_dtypes.py
# smoke tests on auto dtype construction

if dtype.is_signed_integer:
    assert np.dtype(dtype.type).kind == "i"
else:
    assert np.dtype(dtype.type).kind == "u"
assert dtype.name is not None
