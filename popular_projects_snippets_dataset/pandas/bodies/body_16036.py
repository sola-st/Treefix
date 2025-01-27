# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_dropna.py
ser = Series([], dtype=object)

assert len(ser.dropna()) == 0
return_value = ser.dropna(inplace=True)
assert return_value is None
assert len(ser) == 0

# invalid axis
msg = "No axis named 1 for object type Series"
with pytest.raises(ValueError, match=msg):
    ser.dropna(axis=1)
