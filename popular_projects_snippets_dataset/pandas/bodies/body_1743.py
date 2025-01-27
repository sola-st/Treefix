# Extracted from ./data/repos/pandas/pandas/tests/resample/test_datetime_index.py
ts = simple_date_range_series("1/1/1990", "1/1/2000")
ts.index = ts.index.as_unit(unit)

result = ts.resample(freq, kind="period").mean()
expected = ts.resample(freq).mean()
expected.index = period_range(**expected_kwargs)
tm.assert_series_equal(result, expected)
