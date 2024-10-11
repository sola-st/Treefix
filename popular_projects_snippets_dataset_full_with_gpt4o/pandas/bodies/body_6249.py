# Extracted from ./data/repos/pandas/pandas/tests/extension/base/setitem.py
ser = pd.Series(data)
original = ser.copy()
value = [data[0]]
if as_array:
    value = data._from_sequence(value)

xpr = "cannot set using a {} indexer with a different length"
with pytest.raises(ValueError, match=xpr.format("list-like")):
    ser[[0, 1]] = value
# Ensure no modifications made before the exception
self.assert_series_equal(ser, original)

with pytest.raises(ValueError, match=xpr.format("slice")):
    ser[slice(3)] = value
self.assert_series_equal(ser, original)
