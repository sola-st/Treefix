# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
pi = pd.period_range(start="2017-01-01", end="2018-01-01", freq="M")
ser = pi.to_series()
result = ser.loc[:"2017-12"]
expected = ser.iloc[:-1]

tm.assert_series_equal(result, expected)
