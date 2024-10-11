# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
pa_dtype = data_for_grouping.dtype.pyarrow_dtype
with tm.maybe_produces_warning(
    PerformanceWarning,
    pa_version_under7p0 and not pa.types.is_duration(pa_dtype),
    check_stacklevel=False,
):
    super().test_groupby_extension_apply(data_for_grouping, groupby_apply_op)
