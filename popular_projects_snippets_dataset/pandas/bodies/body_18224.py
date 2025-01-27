# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
# rpow does not work with DataFrame
ts = tm.makeTimeSeries()
ts.name = "ts"

df = pd.DataFrame({"A": ts})

tm.assert_series_equal(ts + ts, ts + df["A"], check_names=False)
tm.assert_series_equal(ts**ts, ts ** df["A"], check_names=False)
tm.assert_series_equal(ts < ts, ts < df["A"], check_names=False)
tm.assert_series_equal(ts / ts, ts / df["A"], check_names=False)
