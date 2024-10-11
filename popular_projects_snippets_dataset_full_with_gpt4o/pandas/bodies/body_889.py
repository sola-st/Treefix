# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
arr = index._data.copy()
ser = Series(arr)

self.check_can_hold_element(ser, elem, inplace)

if is_scalar(elem):
    ser[0] = elem
else:
    ser[: len(elem)] = elem

if inplace:
    assert ser.array is arr  # i.e. setting was done inplace
else:
    assert ser.dtype == object
