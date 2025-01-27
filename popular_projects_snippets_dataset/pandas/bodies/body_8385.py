# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
# see gh-9313
rng = date_range("1/1/2013", "7/1/2017", freq=freq)
exp = DatetimeIndex(
    ["2013-12-31", "2014-12-31", "2015-12-31", "2016-12-31"], freq=freq
)
tm.assert_index_equal(rng, exp)
