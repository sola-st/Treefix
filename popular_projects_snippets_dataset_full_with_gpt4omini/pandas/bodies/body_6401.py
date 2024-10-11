# Extracted from ./data/repos/pandas/pandas/tests/extension/test_string.py
with tm.maybe_produces_warning(
    PerformanceWarning,
    pa_version_under7p0 and data.dtype.storage == "pyarrow",
    check_stacklevel=False,
):
    super().test_fillna_no_op_returns_copy(data)
