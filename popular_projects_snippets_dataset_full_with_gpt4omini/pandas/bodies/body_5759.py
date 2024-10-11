# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
pa_dtype = dtype.pyarrow_dtype
if pa.types.is_timestamp(pa_dtype) and pa_dtype.tz is not None:
    request.node.add_marker(
        pytest.mark.xfail(
            raises=NotImplementedError,
            reason=f"pyarrow.type_for_alias cannot infer {pa_dtype}",
        )
    )
elif pa.types.is_string(pa_dtype):
    request.node.add_marker(
        pytest.mark.xfail(
            reason=(
                "Still support StringDtype('pyarrow') "
                "over ArrowDtype(pa.string())"
            ),
        )
    )
super().test_is_dtype_from_name(dtype)
