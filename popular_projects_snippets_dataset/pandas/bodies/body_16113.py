# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_dt_accessor.py
ser = Series(date_range("2018-01-01", periods=10))
ser[2] = None
return_value = ser.fillna(pd.Timestamp("2018-01-01"), inplace=True)
assert return_value is None
result = ser.dt.date
assert result[0] == result[2]
