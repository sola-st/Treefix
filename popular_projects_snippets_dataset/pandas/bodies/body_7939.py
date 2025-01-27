# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_indexing.py
i = period_range("20130101", periods=5, freq="D")
for arr in [np.nan, NaT]:
    result = i.where(notna(i), other=arr)
    expected = i
    tm.assert_index_equal(result, expected)

i2 = i.copy()
i2 = PeriodIndex([NaT, NaT] + i[2:].tolist(), freq="D")
result = i.where(notna(i2), i2)
tm.assert_index_equal(result, i2)

i2 = i.copy()
i2 = PeriodIndex([NaT, NaT] + i[2:].tolist(), freq="D")
result = i.where(notna(i2), i2.values)
tm.assert_index_equal(result, i2)
