# Extracted from ./data/repos/pandas/pandas/tests/arrays/interval/test_interval.py
# GH#45768 The IntervalArray methods raises; the Series method coerces
ser = pd.Series(IntervalArray.from_breaks([1, 2, 3, 4], closed="left"))
mask = np.array([True, False, True])
match = "'value.closed' is 'right', expected 'left'."
with pytest.raises(ValueError, match=match):
    ser.array._where(mask, other)

res = ser.where(mask, other=other)
expected = ser.astype(object).where(mask, other)
tm.assert_series_equal(res, expected)
