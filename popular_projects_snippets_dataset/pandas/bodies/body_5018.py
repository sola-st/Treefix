# Extracted from ./data/repos/pandas/pandas/tests/scalar/test_na_scalar.py
msg = "ufunc method 'at'"
with pytest.raises(ValueError, match=msg):
    np.log.at(NA, 0)
