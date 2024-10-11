# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_combine_first.py
# GH: 37519
df = DataFrame(
    {"a": ["962", "85"], "b": [pd.NA] * 2}, dtype=nullable_string_dtype
)
df2 = DataFrame({"a": ["85"], "b": [pd.NA]}, dtype=nullable_string_dtype)
with tm.maybe_produces_warning(
    PerformanceWarning,
    pa_version_under7p0 and nullable_string_dtype == "string[pyarrow]",
):
    df.set_index(["a", "b"], inplace=True)
with tm.maybe_produces_warning(
    PerformanceWarning,
    pa_version_under7p0 and nullable_string_dtype == "string[pyarrow]",
):
    df2.set_index(["a", "b"], inplace=True)
result = df.combine_first(df2)
with tm.maybe_produces_warning(
    PerformanceWarning,
    pa_version_under7p0 and nullable_string_dtype == "string[pyarrow]",
):
    expected = DataFrame(
        {"a": ["962", "85"], "b": [pd.NA] * 2}, dtype=nullable_string_dtype
    ).set_index(["a", "b"])
tm.assert_frame_equal(result, expected)
