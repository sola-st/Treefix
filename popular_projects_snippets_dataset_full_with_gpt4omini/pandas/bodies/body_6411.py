# Extracted from ./data/repos/pandas/pandas/tests/extension/test_string.py
# GH 25439
with tm.maybe_produces_warning(
    PerformanceWarning,
    pa_version_under7p0
    and getattr(data_missing_for_sorting.dtype, "storage", "") == "pyarrow",
    check_stacklevel=False,
):
    super().test_nargsort(data_missing_for_sorting, na_position, expected)
