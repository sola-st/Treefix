# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
# GH22764
ser = Series([1, 2, np.nan, 3, np.nan, 4])
mask = ser.isna()
median_expected = operation(ser)
median_result = operation(ser, mask=mask)
assert median_expected == median_result
