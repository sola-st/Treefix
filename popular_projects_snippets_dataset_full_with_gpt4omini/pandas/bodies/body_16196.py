# Extracted from ./data/repos/pandas/pandas/tests/series/test_arithmetic.py
# GH#15115
ser = Series([1, 3, 2], index=range(3))
const = 2
result = getattr(ser, opname)(const).dtypes
expected = np.dtype("bool")
assert result == expected
