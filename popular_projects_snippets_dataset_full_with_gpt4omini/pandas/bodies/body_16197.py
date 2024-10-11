# Extracted from ./data/repos/pandas/pandas/tests/series/test_arithmetic.py
# GH#15115 empty Series case
ser = Series([1, 3, 2], index=range(3))
empty = ser.iloc[:0]
const = 2
result = getattr(empty, opname)(const).dtypes
expected = np.dtype("bool")
assert result == expected
