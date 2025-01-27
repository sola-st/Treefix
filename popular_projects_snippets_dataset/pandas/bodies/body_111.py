# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
list_of_valid_strings = ["00:00:01", "00:00:02"]
a = pd.to_timedelta(list_of_valid_strings)
b = Series(list_of_valid_strings).apply(pd.to_timedelta)
tm.assert_series_equal(Series(a), b)

list_of_strings = ["00:00:01", np.nan, pd.NaT, pd.NaT]

a = pd.to_timedelta(list_of_strings)
ser = Series(list_of_strings)
b = ser.apply(pd.to_timedelta)
tm.assert_series_equal(Series(a), b)
