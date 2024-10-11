# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_astype.py
ser = Series(np.random.randn(5), name="foo")
as_typed = ser.astype(dtype)

assert as_typed.dtype == dtype
assert as_typed.name == ser.name
