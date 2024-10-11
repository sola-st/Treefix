# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_timedeltas.py
as_nano = tda._ndarray.astype("m8[ns]")
tda_nano = TimedeltaArray._simple_new(as_nano, dtype=as_nano.dtype)

result = tda.to_pytimedelta()
expected = tda_nano.to_pytimedelta()
tm.assert_numpy_array_equal(result, expected)
