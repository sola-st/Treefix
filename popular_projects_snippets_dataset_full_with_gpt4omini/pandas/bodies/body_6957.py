# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_setops.py
if not index_flat.is_unique:
    pytest.skip("Randomly generated index_flat was not unique.")
index = index_flat

# test copy.union(subset) - need sort for unicode and string
first = index.copy().set_names(fname)
second = index[1:].set_names(sname)
with tm.maybe_produces_warning(
    PerformanceWarning,
    pa_version_under7p0 and getattr(index.dtype, "storage", "") == "pyarrow",
    check_stacklevel=False,
):
    union = first.union(second).sort_values()
with tm.maybe_produces_warning(
    PerformanceWarning,
    pa_version_under7p0 and getattr(index.dtype, "storage", "") == "pyarrow",
    check_stacklevel=False,
):
    expected = index.set_names(expected_name).sort_values()
tm.assert_index_equal(union, expected)
