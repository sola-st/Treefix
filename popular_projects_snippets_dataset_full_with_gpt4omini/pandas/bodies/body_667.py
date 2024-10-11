# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
expected = case.astype(float) if coerce else case.copy()
result, _ = lib.maybe_convert_numeric(
    case,
    set(),
    coerce_numeric=coerce,
    convert_to_masked_nullable=convert_to_masked_nullable,
)

tm.assert_almost_equal(result, expected)
