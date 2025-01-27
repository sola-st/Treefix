# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_fillna.py
# GH#9043
# make sure a string representation of int/float values can be filled
# correctly without raising errors or being converted
vals = ["0", "1.5", "-0.3"]
for val in vals:
    ser = Series([0, 1, np.nan, np.nan, 4], dtype="float64")
    result = ser.fillna(val)
    expected = Series([0, 1, val, val, 4], dtype="object")
    tm.assert_series_equal(result, expected)
