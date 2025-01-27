# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_round.py
# See GH#12600
ser = Series([1.53, 1.36, 0.06], dtype=any_float_dtype)
out = np.round(ser, decimals=0)
expected = Series([2.0, 1.0, 0.0], dtype=any_float_dtype)
tm.assert_series_equal(out, expected)

msg = "the 'out' parameter is not supported"
with pytest.raises(ValueError, match=msg):
    np.round(ser, decimals=0, out=ser)
