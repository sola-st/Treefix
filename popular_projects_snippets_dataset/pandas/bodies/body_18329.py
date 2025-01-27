# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
ser = pd.to_timedelta(Series(["00:00:01"])).astype("m8[s]")

result = ser - NaT
expected = Series([NaT], dtype="m8[s]")
tm.assert_series_equal(result, expected)
