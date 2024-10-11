# Extracted from ./data/repos/pandas/pandas/tests/base/test_value_counts.py
orig = index_or_series_obj
obj = orig.copy()

if not allow_na_ops(obj):
    pytest.skip("type doesn't allow for NA operations")
elif len(obj) < 1:
    pytest.skip("Test doesn't make sense on empty data")
elif isinstance(orig, pd.MultiIndex):
    pytest.skip(f"MultiIndex can't hold '{null_obj}'")

values = obj._values
values[0:2] = null_obj

klass = type(obj)
repeated_values = np.repeat(values, range(1, len(values) + 1))
obj = klass(repeated_values, dtype=obj.dtype)

# because np.nan == np.nan is False, but None == None is True
# np.nan would be duplicated, whereas None wouldn't
counter = collections.Counter(obj.dropna())
expected = Series(dict(counter.most_common()), dtype=np.int64)

if obj.dtype != np.float16:
    expected.index = expected.index.astype(obj.dtype)
else:
    with pytest.raises(NotImplementedError, match="float16 indexes are not "):
        expected.index.astype(obj.dtype)
    exit()

result = obj.value_counts()
if obj.duplicated().any():
    # TODO(GH#32514):
    #  Order of entries with the same count is inconsistent on CI (gh-32449)
    with tm.maybe_produces_warning(
        PerformanceWarning,
        pa_version_under7p0 and getattr(obj.dtype, "storage", "") == "pyarrow",
    ):
        expected = expected.sort_index()
    with tm.maybe_produces_warning(
        PerformanceWarning,
        pa_version_under7p0 and getattr(obj.dtype, "storage", "") == "pyarrow",
    ):
        result = result.sort_index()

if not isinstance(result.dtype, np.dtype):
    # i.e IntegerDtype
    expected = expected.astype("Int64")
tm.assert_series_equal(result, expected)

expected[null_obj] = 3

result = obj.value_counts(dropna=False)
if obj.duplicated().any():
    # TODO(GH#32514):
    #  Order of entries with the same count is inconsistent on CI (gh-32449)
    with tm.maybe_produces_warning(
        PerformanceWarning,
        pa_version_under7p0 and getattr(obj.dtype, "storage", "") == "pyarrow",
    ):
        expected = expected.sort_index()
    with tm.maybe_produces_warning(
        PerformanceWarning,
        pa_version_under7p0 and getattr(obj.dtype, "storage", "") == "pyarrow",
    ):
        result = result.sort_index()
tm.assert_series_equal(result, expected)
