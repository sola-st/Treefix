# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
# GH 40687
arr = np.array([True, np.NaN], dtype=object)
result = libops.maybe_convert_bool(
    arr, set(), convert_to_masked_nullable=convert_to_masked_nullable
)
if convert_to_masked_nullable:
    tm.assert_extension_array_equal(BooleanArray(*result), exp)
else:
    result = result[0]
    tm.assert_numpy_array_equal(result, exp)
