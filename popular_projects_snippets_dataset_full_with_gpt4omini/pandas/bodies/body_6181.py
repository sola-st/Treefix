# Extracted from ./data/repos/pandas/pandas/tests/extension/base/methods.py
assert data[0] != data[1]
cls = type(data)
a, b = data[:2]

orig = pd.Series(cls._from_sequence([a, a, b, b], dtype=data.dtype))
ser = orig.copy()
cond = np.array([True, True, False, False])

if as_frame:
    ser = ser.to_frame(name="a")
    cond = cond.reshape(-1, 1)

result = ser.where(cond)
expected = pd.Series(
    cls._from_sequence([a, a, na_value, na_value], dtype=data.dtype)
)

if as_frame:
    expected = expected.to_frame(name="a")
self.assert_equal(result, expected)

ser.mask(~cond, inplace=True)
self.assert_equal(ser, expected)

# array other
ser = orig.copy()
if as_frame:
    ser = ser.to_frame(name="a")
cond = np.array([True, False, True, True])
other = cls._from_sequence([a, b, a, b], dtype=data.dtype)
if as_frame:
    other = pd.DataFrame({"a": other})
    cond = pd.DataFrame({"a": cond})
result = ser.where(cond, other)
expected = pd.Series(cls._from_sequence([a, b, b, b], dtype=data.dtype))
if as_frame:
    expected = expected.to_frame(name="a")
self.assert_equal(result, expected)

ser.mask(~cond, other, inplace=True)
self.assert_equal(ser, expected)
