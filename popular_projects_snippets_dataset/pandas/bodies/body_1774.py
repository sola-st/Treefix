# Extracted from ./data/repos/pandas/pandas/tests/resample/test_datetime_index.py
# miscellaneous test coverage
len0pts = simple_period_range_series("2007-01", "2010-05", freq="M")[:0]
# it works
result = len0pts.resample("A-DEC").mean()
assert len(result) == 0
