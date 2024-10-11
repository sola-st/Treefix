# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
ea_scalar, ea_dtype = ea_scalar_and_dtype
d = {"a": ea_scalar}
result = Series(d, index=["a"])
expected = Series(ea_scalar, index=["a"], dtype=ea_dtype)

assert result.dtype == ea_dtype

tm.assert_series_equal(result, expected)
