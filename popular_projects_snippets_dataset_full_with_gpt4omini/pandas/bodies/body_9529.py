# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_timedeltas.py
as_nano = tda._ndarray.astype("m8[ns]")
tda_nano = TimedeltaArray._simple_new(as_nano, dtype=as_nano.dtype)

result = getattr(tda, field)
expected = getattr(tda_nano, field)
tm.assert_numpy_array_equal(result, expected)
