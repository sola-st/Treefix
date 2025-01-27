# Extracted from ./data/repos/pandas/pandas/tests/extension/base/accumulate.py
result = getattr(s, op_name)(skipna=skipna)

if result.dtype == pd.Float32Dtype() and op_name == "cumprod" and skipna:
    pytest.skip(
        f"Float32 precision lead to large differences with op {op_name} "
        f"and skipna={skipna}"
    )

expected = getattr(s.astype("float64"), op_name)(skipna=skipna)
self.assert_series_equal(result, expected, check_dtype=False)
