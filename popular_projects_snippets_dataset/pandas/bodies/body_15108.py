# Extracted from ./data/repos/pandas/pandas/tests/base/test_value_counts.py
obj = index_or_series_obj
obj = np.repeat(obj, range(1, len(obj) + 1))
result = obj.value_counts()

counter = collections.Counter(obj)
expected = Series(dict(counter.most_common()), dtype=np.int64, name=obj.name)

if obj.dtype != np.float16:
    expected.index = expected.index.astype(obj.dtype)
else:
    with pytest.raises(NotImplementedError, match="float16 indexes are not "):
        expected.index.astype(obj.dtype)
    exit()

if not isinstance(result.dtype, np.dtype):
    # i.e IntegerDtype
    expected = expected.astype("Int64")

# TODO(GH#32514): Order of entries with the same count is inconsistent
#  on CI (gh-32449)
if obj.duplicated().any():
    with tm.maybe_produces_warning(
        PerformanceWarning,
        pa_version_under7p0 and getattr(obj.dtype, "storage", "") == "pyarrow",
    ):
        result = result.sort_index()
    with tm.maybe_produces_warning(
        PerformanceWarning,
        pa_version_under7p0 and getattr(obj.dtype, "storage", "") == "pyarrow",
    ):
        expected = expected.sort_index()
tm.assert_series_equal(result, expected)
