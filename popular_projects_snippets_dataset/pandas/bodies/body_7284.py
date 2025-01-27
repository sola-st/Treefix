# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/methods/test_astype.py
# GH 13149, GH 13209
idx = TimedeltaIndex([1e14, "NaT", NaT, np.NaN], name="idx")

result = idx.astype(object)
expected = Index(
    [Timedelta("1 days 03:46:40")] + [NaT] * 3, dtype=object, name="idx"
)
tm.assert_index_equal(result, expected)

result = idx.astype(np.int64)
expected = Index(
    [100000000000000] + [-9223372036854775808] * 3, dtype=np.int64, name="idx"
)
tm.assert_index_equal(result, expected)

result = idx.astype(str)
expected = Index([str(x) for x in idx], name="idx")
tm.assert_index_equal(result, expected)

rng = timedelta_range("1 days", periods=10)
result = rng.astype("i8")
tm.assert_index_equal(result, Index(rng.asi8))
tm.assert_numpy_array_equal(rng.asi8, result.values)
