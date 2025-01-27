# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_clip.py
# GH-42794
ser = Series([datetime(1, 1, 1), datetime(9999, 9, 9)])

result = ser.clip(lower=Timestamp.min, upper=Timestamp.max)
expected = Series([Timestamp.min, Timestamp.max], dtype="object")

tm.assert_series_equal(result, expected)
