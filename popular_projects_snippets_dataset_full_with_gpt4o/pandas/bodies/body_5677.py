# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
exp = Series([2**63], dtype=np.uint64)
ser = Series([1, 2**63, 2**63], dtype=np.uint64)
tm.assert_numpy_array_equal(algos.mode(ser.values), exp.values)
tm.assert_series_equal(ser.mode(), exp)

exp = Series([1, 2**63], dtype=np.uint64)
ser = Series([1, 2**63], dtype=np.uint64)
tm.assert_numpy_array_equal(algos.mode(ser.values), exp.values)
tm.assert_series_equal(ser.mode(), exp)
