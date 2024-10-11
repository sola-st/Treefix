# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
pa_dtype = ser.dtype.pyarrow_dtype
if op_name == "count":
    result = getattr(ser, op_name)()
else:
    result = getattr(ser, op_name)(skipna=skipna)
if pa.types.is_boolean(pa_dtype):
    # Can't convert if ser contains NA
    pytest.skip(
        "pandas boolean data with NA does not fully support all reductions"
    )
elif pa.types.is_integer(pa_dtype) or pa.types.is_floating(pa_dtype):
    ser = ser.astype("Float64")
if op_name == "count":
    expected = getattr(ser, op_name)()
else:
    expected = getattr(ser, op_name)(skipna=skipna)
tm.assert_almost_equal(result, expected)
