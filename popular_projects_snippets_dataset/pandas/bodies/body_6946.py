# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_setops.py
# Union with a non-unique, non-monotonic index raises error
# Only needed for bool index factory
with tm.maybe_produces_warning(
    PerformanceWarning,
    pa_version_under7p0 and getattr(index.dtype, "storage", "") == "pyarrow",
    check_stacklevel=False,
):
    idx1 = index.sort_values()
with tm.maybe_produces_warning(
    PerformanceWarning,
    pa_version_under7p0 and getattr(index.dtype, "storage", "") == "pyarrow",
    check_stacklevel=False,
):
    idx2 = index.sort_values()
assert idx1.union(idx2).dtype == idx1.dtype
