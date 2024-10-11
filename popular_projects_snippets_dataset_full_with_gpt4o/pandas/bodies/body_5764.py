# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
with tm.maybe_produces_warning(
    PerformanceWarning, pa_version_under6p0, check_stacklevel=False
):
    super().test_dropna_array(data_missing)
