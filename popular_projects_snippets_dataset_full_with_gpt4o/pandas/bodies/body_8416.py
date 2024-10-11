# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
# GH 23270
tz = tz_aware_fixture
result = date_range(start="2011-06-01", end="2011-01-01", freq="-1MS", tz=tz)
expected = date_range(end="2011-06-01", start="2011-01-01", freq="1MS", tz=tz)[
    ::-1
]
tm.assert_index_equal(result, expected)
