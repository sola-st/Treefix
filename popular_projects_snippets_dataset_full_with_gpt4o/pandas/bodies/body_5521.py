# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_arithmetic.py
# GH#33296
ts = Timestamp("2020-04-04 15:45", tz="US/Pacific")

other = np.arange(6).astype("m8[h]").reshape(shape)

result = ts + other

ex_stamps = [ts + Timedelta(hours=n) for n in range(6)]
expected = np.array(ex_stamps).reshape(shape)
tm.assert_numpy_array_equal(result, expected)

result = other + ts
tm.assert_numpy_array_equal(result, expected)

result = ts - other
ex_stamps = [ts - Timedelta(hours=n) for n in range(6)]
expected = np.array(ex_stamps).reshape(shape)
tm.assert_numpy_array_equal(result, expected)

msg = r"unsupported operand type\(s\) for -: 'numpy.ndarray' and 'Timestamp'"
with pytest.raises(TypeError, match=msg):
    other - ts
