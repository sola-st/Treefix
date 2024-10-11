# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
# GH#32684 a scalar key that is not recognized by lib.is_scalar

# a series that might be produced via `frame.dtypes`
ser = Series([1, 2], index=[np.dtype("O"), np.dtype("i8")])

key = ser.index[1]

result = ser[key]
assert result == 2
