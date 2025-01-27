# Extracted from ./data/repos/pandas/pandas/tests/resample/test_datetime_index.py
s = series
s.index = s.index.as_unit(unit)
result = s.resample("5Min").last()
grouper = Grouper(freq=Minute(5), closed="left", label="left")
expected = s.groupby(grouper).agg(lambda x: x[-1])
tm.assert_series_equal(result, expected)
