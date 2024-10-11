# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
with tm.maybe_produces_warning(
    PerformanceWarning,
    pa_version_under7p0 and getattr(index.dtype, "storage", "") == "pyarrow",
    check_stacklevel=False,
):
    super().test_argsort(index)
