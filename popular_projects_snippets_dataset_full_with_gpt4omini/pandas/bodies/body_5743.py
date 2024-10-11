# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
pa_dtype = data.dtype.pyarrow_dtype
if (pa.types.is_timestamp(pa_dtype) and pa_dtype.tz) or pa.types.is_string(
    pa_dtype
):
    if pa.types.is_string(pa_dtype):
        reason = "ArrowDtype(pa.string()) != StringDtype('pyarrow')"
    else:
        reason = f"pyarrow.type_for_alias cannot infer {pa_dtype}"
    request.node.add_marker(
        pytest.mark.xfail(
            reason=reason,
        )
    )
super().test_from_dtype(data)
