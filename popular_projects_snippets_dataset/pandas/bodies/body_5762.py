# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
pa_dtype = dtype.pyarrow_dtype
if (
    pa.types.is_date(pa_dtype)
    or pa.types.is_time(pa_dtype)
    or (
        pa.types.is_timestamp(pa_dtype)
        and (pa_dtype.unit != "ns" or pa_dtype.tz is not None)
    )
    or (pa.types.is_duration(pa_dtype) and pa_dtype.unit != "ns")
    or pa.types.is_string(pa_dtype)
    or pa.types.is_binary(pa_dtype)
):
    request.node.add_marker(
        pytest.mark.xfail(
            reason=(
                f"{pa_dtype} does not have associated numpy "
                f"dtype findable by find_common_type"
            )
        )
    )
super().test_get_common_dtype(dtype)
