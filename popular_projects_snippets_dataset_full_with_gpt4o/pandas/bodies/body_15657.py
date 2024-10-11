# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_interpolate.py
# GH#36624
ser = Series([1, 3, np.nan, 12, np.nan, 25])

msg = "Cannot pass both fill_value and method"
with pytest.raises(ValueError, match=msg):
    ser.interpolate(fill_value=3, method="pad")
