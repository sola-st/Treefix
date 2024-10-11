# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_period.py
# GH#45768 The PeriodArray method raises, the Series method coerces
ser = pd.Series(period_array(["2000", "2001", "2002"], freq="D"))
cond = np.array([True, False, True])

with pytest.raises(IncompatibleFrequency, match="freq"):
    ser.array._where(cond, other)

res = ser.where(cond, other)
expected = ser.astype(object).where(cond, other)
tm.assert_series_equal(res, expected)
