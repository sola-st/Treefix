# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_copy.py
# don't want to be able to modify the index stored elsewhere after
# making a copy

datetime_series.index.name = None
assert datetime_series.index.name is None
assert datetime_series is datetime_series

cp = datetime_series.copy()
cp.index.name = "foo"
assert datetime_series.index.name is None
