# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_align.py
a, b = datetime_series.align(datetime_series, copy=False)
assert a.index is datetime_series.index
assert b.index is datetime_series.index

a, b = datetime_series.align(datetime_series, copy=True)
assert a.index is not datetime_series.index
assert b.index is not datetime_series.index
