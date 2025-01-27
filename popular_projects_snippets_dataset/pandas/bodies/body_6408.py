# Extracted from ./data/repos/pandas/pandas/tests/extension/test_string.py
all_data = all_data[:10]
if dropna:
    other = all_data[~all_data.isna()]
else:
    other = all_data
with tm.maybe_produces_warning(
    PerformanceWarning,
    pa_version_under7p0
    and getattr(all_data.dtype, "storage", "") == "pyarrow"
    and not (dropna and "data_missing" in request.node.nodeid),
):
    result = pd.Series(all_data).value_counts(dropna=dropna).sort_index()
with tm.maybe_produces_warning(
    PerformanceWarning,
    pa_version_under7p0
    and getattr(other.dtype, "storage", "") == "pyarrow"
    and not (dropna and "data_missing" in request.node.nodeid),
):
    expected = pd.Series(other).value_counts(dropna=dropna).sort_index()

self.assert_series_equal(result, expected)
