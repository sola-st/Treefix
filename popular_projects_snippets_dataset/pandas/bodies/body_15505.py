# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_round.py
# GH14940
ser = Series([pd.NaT])
expected = Series(pd.NaT)
round_method = getattr(ser.dt, method)
tm.assert_series_equal(round_method(freq), expected)
