# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
ix = timedelta_range(start="1 day", end="2 days", freq="1H")
ser = ix.to_series()
result = ser.loc[:"1 days"]
expected = ser.iloc[:-1]

tm.assert_series_equal(result, expected)
