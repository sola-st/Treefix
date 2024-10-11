# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
arr = np.array([2**63, 2**63 + 1], dtype=object)
na_values = {2**63}

expected = (
    np.array([np.nan, 2**63 + 1], dtype=float) if coerce else arr.copy()
)
result = lib.maybe_convert_numeric(
    arr,
    na_values,
    coerce_numeric=coerce,
    convert_to_masked_nullable=convert_to_masked_nullable,
)
if convert_to_masked_nullable and coerce:
    expected = IntegerArray(
        np.array([0, 2**63 + 1], dtype="u8"),
        np.array([True, False], dtype="bool"),
    )
    result = IntegerArray(*result)
else:
    result = result[0]  # discard mask
tm.assert_almost_equal(result, expected)
