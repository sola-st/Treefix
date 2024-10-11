# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_coercion.py
# GH35865 - int casted to str when internally calling np.array(ser.values)
ser = pd.Series(["a", 1])
ser[:] = list(ser.values)

expected = pd.Series(["a", 1])

tm.assert_series_equal(ser, expected)
