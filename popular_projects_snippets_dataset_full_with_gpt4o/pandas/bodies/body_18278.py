# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_object.py
ser = Series(np.random.randn(10), dtype=object)
shifted = ser.shift(2)

func = comparison_op

result = func(ser, shifted)
expected = func(ser.astype(float), shifted.astype(float))
tm.assert_series_equal(result, expected)
