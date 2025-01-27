# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_argsort.py
func = getattr(np, name)
tm.assert_numpy_array_equal(
    func(ser).values, func(np.array(ser)), check_dtype=check_dtype
)

# with missing values
ts = ser.copy()
ts[::2] = np.NaN

result = func(ts)[1::2]
expected = func(np.array(ts.dropna()))

tm.assert_numpy_array_equal(result.values, expected, check_dtype=False)
