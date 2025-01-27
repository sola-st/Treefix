# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/methods/test_astype.py
# GH#13149, GH#13209
idx = PeriodIndex(["2016-05-16", "NaT", NaT, np.NaN], freq="D", name="idx")

result = idx.astype(object)
expected = Index(
    [Period("2016-05-16", freq="D")] + [Period(NaT, freq="D")] * 3,
    dtype="object",
    name="idx",
)
tm.assert_index_equal(result, expected)

result = idx.astype(np.int64)
expected = Index(
    [16937] + [-9223372036854775808] * 3, dtype=np.int64, name="idx"
)
tm.assert_index_equal(result, expected)

result = idx.astype(str)
expected = Index([str(x) for x in idx], name="idx")
tm.assert_index_equal(result, expected)

idx = period_range("1990", "2009", freq="A", name="idx")
result = idx.astype("i8")
tm.assert_index_equal(result, Index(idx.asi8, name="idx"))
tm.assert_numpy_array_equal(result.values, idx.asi8)
