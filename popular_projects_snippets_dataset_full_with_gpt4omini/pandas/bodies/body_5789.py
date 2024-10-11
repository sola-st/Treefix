# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
mark = None

arrow_temporal_supported = self._is_temporal_supported(opname, pa_dtype)

if (
    opname == "__rpow__"
    and (pa.types.is_floating(pa_dtype) or pa.types.is_integer(pa_dtype))
    and not pa_version_under6p0
):
    mark = pytest.mark.xfail(
        reason=(
            f"GH#29997: 1**pandas.NA == 1 while 1**pyarrow.NA == NULL "
            f"for {pa_dtype}"
        )
    )
elif arrow_temporal_supported:
    mark = pytest.mark.xfail(
        raises=TypeError,
        reason=(
            f"{opname} not supported between"
            f"pd.NA and {pa_dtype} Python scalar"
        ),
    )
elif (
    opname in {"__rtruediv__", "__rfloordiv__"}
    and (pa.types.is_floating(pa_dtype) or pa.types.is_integer(pa_dtype))
    and not pa_version_under6p0
):
    mark = pytest.mark.xfail(
        raises=pa.ArrowInvalid,
        reason="divide by 0",
    )

exit(mark)
