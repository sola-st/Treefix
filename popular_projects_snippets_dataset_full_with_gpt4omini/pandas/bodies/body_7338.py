# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_indexing.py
tdi = timedelta_range("1 day", periods=3, freq="D", name="idx")

tail = tdi[2:].tolist()
i2 = Index([NaT, NaT] + tail)
mask = notna(i2)

expected = Index([NaT.value, NaT.value] + tail, dtype=object, name="idx")
assert isinstance(expected[0], int)
result = tdi.where(mask, i2.asi8)
tm.assert_index_equal(result, expected)

ts = i2 + fixed_now_ts
expected = Index([ts[0], ts[1]] + tail, dtype=object, name="idx")
result = tdi.where(mask, ts)
tm.assert_index_equal(result, expected)

per = (i2 + fixed_now_ts).to_period("D")
expected = Index([per[0], per[1]] + tail, dtype=object, name="idx")
result = tdi.where(mask, per)
tm.assert_index_equal(result, expected)

ts = fixed_now_ts
expected = Index([ts, ts] + tail, dtype=object, name="idx")
result = tdi.where(mask, ts)
tm.assert_index_equal(result, expected)
