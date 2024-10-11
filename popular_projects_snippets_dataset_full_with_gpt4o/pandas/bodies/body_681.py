# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
# GH 40687
arr = np.array([2.0, np.nan], dtype=object)
result = lib.maybe_convert_numeric(
    arr, set(), convert_to_masked_nullable=convert_to_masked_nullable
)
if convert_to_masked_nullable:
    tm.assert_extension_array_equal(FloatingArray(*result), exp)
else:
    result = result[0]
    tm.assert_numpy_array_equal(result, exp)
