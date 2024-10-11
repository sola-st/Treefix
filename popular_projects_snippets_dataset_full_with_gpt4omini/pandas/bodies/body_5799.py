# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
pa_dtype = data_for_grouping.dtype.pyarrow_dtype
if pa.types.is_string(pa_dtype) or pa.types.is_binary(pa_dtype):
    request.node.add_marker(
        pytest.mark.xfail(
            raises=pa.ArrowNotImplementedError,
            reason=f"mode not supported by pyarrow for {pa_dtype}",
        )
    )
elif (
    pa.types.is_boolean(pa_dtype)
    and "multi_mode" in request.node.nodeid
    and pa_version_under9p0
):
    request.node.add_marker(
        pytest.mark.xfail(
            reason="https://issues.apache.org/jira/browse/ARROW-17096",
        )
    )
data = data_for_grouping.take(take_idx)
ser = pd.Series(data)
result = ser.mode(dropna=dropna)
expected = pd.Series(data_for_grouping.take(exp_idx))
tm.assert_series_equal(result, expected)
