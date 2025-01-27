# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
# see gh-13274
result, _ = lib.maybe_convert_numeric(
    np.array([prefix + infinity], dtype=object),
    na_values={"", "NULL", "nan"},
    coerce_numeric=coerce_numeric,
    convert_to_masked_nullable=convert_to_masked_nullable,
)
expected = np.array([np.inf if prefix in ["", "+"] else -np.inf])
tm.assert_numpy_array_equal(result, expected)
