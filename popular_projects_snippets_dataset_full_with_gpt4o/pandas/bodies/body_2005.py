# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
# Cannot cast to an integer (signed or unsigned)
# because we have a float number.
res = to_numeric(data, downcast=downcast)
tm.assert_numpy_array_equal(res, expected)
