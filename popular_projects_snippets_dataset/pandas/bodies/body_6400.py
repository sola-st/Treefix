# Extracted from ./data/repos/pandas/pandas/tests/extension/test_string.py
with tm.maybe_produces_warning(
    PerformanceWarning,
    pa_version_under6p0 and data_missing.dtype.storage == "pyarrow",
):
    result = data_missing.dropna()
expected = data_missing[[1]]
self.assert_extension_array_equal(result, expected)
