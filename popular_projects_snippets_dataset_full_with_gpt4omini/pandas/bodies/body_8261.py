# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_astype.py
# GH 13149, GH 13209
idx = DatetimeIndex(["2016-05-16", "NaT", NaT, np.NaN], name="idx")

result = idx.astype(object)
expected = Index(
    [Timestamp("2016-05-16")] + [NaT] * 3, dtype=object, name="idx"
)
tm.assert_index_equal(result, expected)

result = idx.astype(np.int64)
expected = Index(
    [1463356800000000000] + [-9223372036854775808] * 3,
    dtype=np.int64,
    name="idx",
)
tm.assert_index_equal(result, expected)

rng = date_range("1/1/2000", periods=10, name="idx")
result = rng.astype("i8")
tm.assert_index_equal(result, Index(rng.asi8, name="idx"))
tm.assert_numpy_array_equal(result.values, rng.asi8)
