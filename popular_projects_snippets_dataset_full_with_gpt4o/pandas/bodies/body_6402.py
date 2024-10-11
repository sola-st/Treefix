# Extracted from ./data/repos/pandas/pandas/tests/extension/test_string.py
with tm.maybe_produces_warning(
    PerformanceWarning,
    pa_version_under7p0 and data_missing.dtype.storage == "pyarrow",
    check_stacklevel=False,
):
    super().test_fillna_series_method(data_missing, fillna_method)
