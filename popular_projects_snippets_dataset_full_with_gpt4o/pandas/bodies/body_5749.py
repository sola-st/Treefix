# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
pa_type = data.dtype.pyarrow_dtype
if (
    (pa.types.is_integer(pa_type) or pa.types.is_floating(pa_type))
    and all_numeric_accumulations == "cumsum"
    and not pa_version_under9p0
):
    pytest.skip("These work, are tested by test_accumulate_series.")

op_name = all_numeric_accumulations
ser = pd.Series(data)

with pytest.raises(NotImplementedError):
    getattr(ser, op_name)(skipna=skipna)
