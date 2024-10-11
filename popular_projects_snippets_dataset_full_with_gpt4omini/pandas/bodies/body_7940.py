# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_indexing.py
pi = period_range("20130101", periods=5, freq="D")

tail = pi[2:].tolist()
i2 = PeriodIndex([NaT, NaT] + tail, freq="D")
mask = notna(i2)

result = pi.where(mask, i2.asi8)
expected = pd.Index([NaT.value, NaT.value] + tail, dtype=object)
assert isinstance(expected[0], int)
tm.assert_index_equal(result, expected)

tdi = i2.asi8.view("timedelta64[ns]")
expected = pd.Index([tdi[0], tdi[1]] + tail, dtype=object)
assert isinstance(expected[0], np.timedelta64)
result = pi.where(mask, tdi)
tm.assert_index_equal(result, expected)

dti = i2.to_timestamp("S")
expected = pd.Index([dti[0], dti[1]] + tail, dtype=object)
assert expected[0] is NaT
result = pi.where(mask, dti)
tm.assert_index_equal(result, expected)

td = Timedelta(days=4)
expected = pd.Index([td, td] + tail, dtype=object)
assert expected[0] == td
result = pi.where(mask, td)
tm.assert_index_equal(result, expected)
