# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
arr = np.arange(5).astype(dtype)
ser = Series(arr)
ser = ser.astype(object)
ser.values[0] = np.timedelta64(4, "ns")
exit(ser)
