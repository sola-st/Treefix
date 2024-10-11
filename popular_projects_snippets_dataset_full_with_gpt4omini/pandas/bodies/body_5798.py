# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
pa_dtype = data.dtype.pyarrow_dtype

data = data.take([0, 0, 0])
ser = pd.Series(data)

if (
    pa.types.is_string(pa_dtype)
    or pa.types.is_binary(pa_dtype)
    or pa.types.is_boolean(pa_dtype)
):
    # For string, bytes, and bool, we don't *expect* to have quantile work
    # Note this matches the non-pyarrow behavior
    if pa_version_under7p0:
        msg = r"Function quantile has no kernel matching input types \(.*\)"
    else:
        msg = r"Function 'quantile' has no kernel matching input types \(.*\)"
    with pytest.raises(pa.ArrowNotImplementedError, match=msg):
        ser.quantile(q=quantile, interpolation=interpolation)
    exit()

if pa.types.is_integer(pa_dtype) or pa.types.is_floating(pa_dtype):
    pass
elif pa.types.is_temporal(data._data.type) and interpolation in ["lower", "higher"]:
    pass
else:
    request.node.add_marker(
        pytest.mark.xfail(
            raises=pa.ArrowNotImplementedError,
            reason=f"quantile not supported by pyarrow for {pa_dtype}",
        )
    )
data = data.take([0, 0, 0])
ser = pd.Series(data)
result = ser.quantile(q=quantile, interpolation=interpolation)
if quantile == 0.5:
    assert result == data[0]
else:
    # Just check the values
    expected = pd.Series(data.take([0, 0]), index=[0.5, 0.5])
    if pa.types.is_integer(pa_dtype) or pa.types.is_floating(pa_dtype):
        expected = expected.astype("float64[pyarrow]")
        result = result.astype("float64[pyarrow]")
    tm.assert_series_equal(result, expected)
