# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_astype.py
ser = Series(date_range("20130101", periods=3, tz="US/Eastern"))

# astype
result = ser.astype(object)
expected = Series(ser.astype(object), dtype=object)
tm.assert_series_equal(result, expected)

result = Series(ser.values).dt.tz_localize("UTC").dt.tz_convert(ser.dt.tz)
tm.assert_series_equal(result, ser)

# astype - object, preserves on construction
result = Series(ser.astype(object))
expected = ser.astype(object)
tm.assert_series_equal(result, expected)

# astype - datetime64[ns, tz]
msg = "Cannot use .astype to convert from timezone-naive"
with pytest.raises(TypeError, match=msg):
    # dt64->dt64tz astype deprecated
    Series(ser.values).astype("datetime64[ns, US/Eastern]")

with pytest.raises(TypeError, match=msg):
    # dt64->dt64tz astype deprecated
    Series(ser.values).astype(ser.dtype)

result = ser.astype("datetime64[ns, CET]")
expected = Series(date_range("20130101 06:00:00", periods=3, tz="CET"))
tm.assert_series_equal(result, expected)
