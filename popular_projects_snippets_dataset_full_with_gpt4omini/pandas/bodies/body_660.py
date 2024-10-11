# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
# see gh-13314
data = np.array(["1.200", "-999.000", "4.500"], dtype=object)
expected = np.array([1.2, np.nan, 4.5], dtype=np.float64)
nan_values = {-999, -999.0}

out = lib.maybe_convert_numeric(
    data,
    nan_values,
    coerce,
    convert_to_masked_nullable=convert_to_masked_nullable,
)
if convert_to_masked_nullable:
    expected = FloatingArray(expected, np.isnan(expected))
    tm.assert_extension_array_equal(expected, FloatingArray(*out))
else:
    out = out[0]
    tm.assert_numpy_array_equal(out, expected)
