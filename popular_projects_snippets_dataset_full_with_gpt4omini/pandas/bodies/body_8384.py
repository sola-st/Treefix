# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
# see gh-9313
rng = date_range("1/1/2013", "7/1/2017", freq=freq)
exp = DatetimeIndex(
    ["2013-01-01", "2014-01-01", "2015-01-01", "2016-01-01", "2017-01-01"],
    freq=freq,
)
tm.assert_index_equal(rng, exp)
