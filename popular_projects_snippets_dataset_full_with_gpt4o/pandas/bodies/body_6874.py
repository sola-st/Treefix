# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_common.py
# GH#12309: Check that the "name" argument
# passed at initialization is honored.
index = index_flat

first = type(index)(index, copy=True, name="mario")
second = type(first)(first, copy=False)

# Even though "copy=False", we want a new object.
assert first is not second
tm.assert_index_equal(first, second)

# Not using tm.assert_index_equal() since names differ.
assert index.equals(first)

assert first.name == "mario"
assert second.name == "mario"

# TODO: belongs in series arithmetic tests?
s1 = pd.Series(2, index=first)
s2 = pd.Series(3, index=second[:-1])
# See GH#13365
with tm.maybe_produces_warning(
    PerformanceWarning,
    pa_version_under7p0 and getattr(index.dtype, "storage", "") == "pyarrow",
    check_stacklevel=False,
):
    s3 = s1 * s2
assert s3.index.name == "mario"
