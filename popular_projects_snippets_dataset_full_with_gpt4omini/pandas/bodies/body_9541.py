# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_timedeltas.py
other = np.arange(len(tda))
result = tda / other
expected = TimedeltaArray._simple_new(tda._ndarray / other, dtype=tda.dtype)
tm.assert_extension_array_equal(result, expected)
assert result._creso == tda._creso
