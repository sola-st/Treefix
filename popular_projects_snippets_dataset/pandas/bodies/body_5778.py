# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
with tm.maybe_produces_warning(
    PerformanceWarning, pa_version_under7p0, check_stacklevel=False
):
    super().test_sort_values(data_for_sorting, ascending, sort_by_key)
