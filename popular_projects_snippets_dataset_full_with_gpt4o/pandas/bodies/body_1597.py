# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
ser = index.to_series()
result = ser.loc[: index[-2]]
expected = ser.iloc[:-1]

tm.assert_series_equal(result, expected)
