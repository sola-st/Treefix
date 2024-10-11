# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
tz = tz_naive_fixture
# GH 6961
rng1 = date_range("2014", "2015", freq="M", tz=tz)
expected1 = date_range("2014-01-31", "2014-12-31", freq="M", tz=tz)

rng2 = date_range("2014", "2015", freq="MS", tz=tz)
expected2 = date_range("2014-01-01", "2015-01-01", freq="MS", tz=tz)

rng3 = date_range("2014", "2020", freq="A", tz=tz)
expected3 = date_range("2014-12-31", "2019-12-31", freq="A", tz=tz)

rng4 = date_range("2014", "2020", freq="AS", tz=tz)
expected4 = date_range("2014-01-01", "2020-01-01", freq="AS", tz=tz)

for rng, expected in [
    (rng1, expected1),
    (rng2, expected2),
    (rng3, expected3),
    (rng4, expected4),
]:
    tm.assert_index_equal(rng, expected)
