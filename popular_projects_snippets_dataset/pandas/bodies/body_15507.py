# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_repeat.py
ser = Series(np.arange(3), name="x")
expected = Series(
    ser.values.repeat(2), name="x", index=ser.index.values.repeat(2)
)
tm.assert_series_equal(np.repeat(ser, 2), expected)

msg = "the 'axis' parameter is not supported"
with pytest.raises(ValueError, match=msg):
    np.repeat(ser, 2, axis=0)
