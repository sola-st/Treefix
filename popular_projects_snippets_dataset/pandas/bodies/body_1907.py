# Extracted from ./data/repos/pandas/pandas/tests/resample/test_period_index.py
ts = simple_period_range_series("1/1/1990", "12/31/1995", freq="M")

result = ts.resample("A-DEC", kind="timestamp").mean()
expected = ts.to_timestamp(how="start").resample("A-DEC").mean()
tm.assert_series_equal(result, expected)
