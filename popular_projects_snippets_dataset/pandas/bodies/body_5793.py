# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
pa_dtype = data.dtype.pyarrow_dtype
if not (
    pa.types.is_integer(pa_dtype)
    or pa.types.is_floating(pa_dtype)
    or (not pa_version_under8p0 and pa.types.is_duration(pa_dtype))
):
    request.node.add_marker(
        pytest.mark.xfail(
            raises=NotImplementedError,
            reason=f"add_checked not implemented for {pa_dtype}",
        )
    )
elif pa_dtype.equals("int8"):
    request.node.add_marker(
        pytest.mark.xfail(
            raises=pa.ArrowInvalid,
            reason=f"raises on overflow for {pa_dtype}",
        )
    )
super().test_add_series_with_extension_array(data)
