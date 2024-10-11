# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval.py
values = IntervalIndex([Interval(0, 1), Interval(1, 2)])
msg = "'<' not supported between instances of 'pandas._libs.interval.Interval' and "
with pytest.raises(TypeError, match=msg):
    values.searchsorted(arg)
