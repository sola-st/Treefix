# Extracted from ./data/repos/pandas/pandas/tests/extension/base/missing.py
fill_value = data_missing[1]
ser = pd.Series(data_missing)

result = ser.fillna(fill_value)
expected = pd.Series(
    data_missing._from_sequence(
        [fill_value, fill_value], dtype=data_missing.dtype
    )
)
self.assert_series_equal(result, expected)

# Fill with a series
result = ser.fillna(expected)
self.assert_series_equal(result, expected)

# Fill with a series not affecting the missing values
result = ser.fillna(ser)
self.assert_series_equal(result, ser)
