# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_timedelta.py
# pre-2.0 td64 astype converted to float64. now for supported units
#  (s, ms, us, ns) this converts to the requested dtype.
# This matches TDA and Series
tdi = timedelta_range("1 Day", periods=30)

res = tdi.astype("m8[s]")
exp_values = np.asarray(tdi).astype("m8[s]")
exp_tda = TimedeltaArray._simple_new(
    exp_values, dtype=exp_values.dtype, freq=tdi.freq
)
expected = Index(exp_tda)
assert expected.dtype == "m8[s]"
tm.assert_index_equal(res, expected)

# check this matches Series and TimedeltaArray
res = tdi._data.astype("m8[s]")
tm.assert_equal(res, expected._values)

res = tdi.to_series().astype("m8[s]")
tm.assert_equal(res._values, expected._values._with_freq(None))
