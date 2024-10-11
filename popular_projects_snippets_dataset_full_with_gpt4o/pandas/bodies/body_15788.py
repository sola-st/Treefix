# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_astype.py
ser = Series(iNaT, dtype="M8[ns]", index=range(5))

ser = ser.astype("O")
assert ser.dtype == np.object_

ser = Series([datetime(2001, 1, 2, 0, 0)])

ser = ser.astype("O")
assert ser.dtype == np.object_

ser = Series([datetime(2001, 1, 2, 0, 0) for i in range(3)])

ser[1] = np.nan
assert ser.dtype == "M8[ns]"

ser = ser.astype("O")
assert ser.dtype == np.object_
