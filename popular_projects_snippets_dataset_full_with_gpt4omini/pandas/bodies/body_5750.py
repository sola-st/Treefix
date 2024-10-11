# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
pa_type = data.dtype.pyarrow_dtype
op_name = all_numeric_accumulations
ser = pd.Series(data)

do_skip = False
if pa.types.is_string(pa_type) or pa.types.is_binary(pa_type):
    if op_name in ["cumsum", "cumprod"]:
        do_skip = True
elif pa.types.is_temporal(pa_type) and not pa.types.is_duration(pa_type):
    if op_name in ["cumsum", "cumprod"]:
        do_skip = True
elif pa.types.is_duration(pa_type):
    if op_name == "cumprod":
        do_skip = True

if do_skip:
    pytest.skip(
        "These should *not* work, we test in test_accumulate_series_raises "
        "that these correctly raise."
    )

if all_numeric_accumulations != "cumsum" or pa_version_under9p0:
    request.node.add_marker(
        pytest.mark.xfail(
            reason=f"{all_numeric_accumulations} not implemented",
            raises=NotImplementedError,
        )
    )
elif all_numeric_accumulations == "cumsum" and (
    pa.types.is_duration(pa_type) or pa.types.is_boolean(pa_type)
):
    request.node.add_marker(
        pytest.mark.xfail(
            reason=f"{all_numeric_accumulations} not implemented for {pa_type}",
            raises=NotImplementedError,
        )
    )

self.check_accumulate(ser, op_name, skipna)
