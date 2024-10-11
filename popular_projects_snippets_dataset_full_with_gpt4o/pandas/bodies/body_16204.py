# Extracted from ./data/repos/pandas/pandas/tests/series/test_arithmetic.py
ser = Series(bdate_range("1/1/2000", periods=10), dtype=object)
ser[::2] = np.nan

# test that comparisons work
val = ser[5]

result = comparison_op(ser, val)
expected = comparison_op(ser.dropna(), val).reindex(ser.index)

if comparison_op is operator.ne:
    expected = expected.fillna(True).astype(bool)
else:
    expected = expected.fillna(False).astype(bool)

tm.assert_series_equal(result, expected)
