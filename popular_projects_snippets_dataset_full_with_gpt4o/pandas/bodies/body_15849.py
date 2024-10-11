# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
ser = pd.Series([0, 1, 2, 3, 4])
result = ser.replace([1, 2, 3])
tm.assert_series_equal(result, pd.Series([0, 0, 0, 0, 4]))

s = ser.copy()
return_value = s.replace([1, 2, 3], inplace=True)
assert return_value is None
tm.assert_series_equal(s, pd.Series([0, 0, 0, 0, 4]))

# make sure things don't get corrupted when fillna call fails
s = ser.copy()
msg = (
    r"Invalid fill method\. Expecting pad \(ffill\) or backfill "
    r"\(bfill\)\. Got crash_cymbal"
)
with pytest.raises(ValueError, match=msg):
    return_value = s.replace([1, 2, 3], inplace=True, method="crash_cymbal")
    assert return_value is None
tm.assert_series_equal(s, ser)
