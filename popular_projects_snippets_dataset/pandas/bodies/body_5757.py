# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
pa_dtype = data_for_grouping.dtype.pyarrow_dtype
if pa.types.is_boolean(pa_dtype):
    request.node.add_marker(
        pytest.mark.xfail(
            raises=ValueError,
            reason=f"{pa_dtype} only has 2 unique possible values",
        )
    )
with tm.maybe_produces_warning(
    PerformanceWarning,
    pa_version_under7p0 and not pa.types.is_duration(pa_dtype),
    check_stacklevel=False,
):
    super().test_groupby_extension_agg(as_index, data_for_grouping)
