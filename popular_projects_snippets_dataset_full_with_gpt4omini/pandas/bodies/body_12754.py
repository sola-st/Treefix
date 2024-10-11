# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
date_unit = "ns"

# freq doesn't round-trip
rng = DatetimeIndex(list(date_range("1/1/2000", periods=20)), freq=None)
encoded = ujson.encode(rng, date_unit=date_unit)

decoded = DatetimeIndex(np.array(ujson.decode(encoded)))
tm.assert_index_equal(rng, decoded)

ts = Series(np.random.randn(len(rng)), index=rng)
decoded = Series(ujson.decode(ujson.encode(ts, date_unit=date_unit)))

idx_values = decoded.index.values.astype(np.int64)
decoded.index = DatetimeIndex(idx_values)
tm.assert_series_equal(ts, decoded)
