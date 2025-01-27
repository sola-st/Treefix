# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
start = "2020-01-01"
end = "2020-01-11"
rng1 = date_range(start, end, freq="3D")
rng2 = date_range(start, end, freq=timedelta(days=3))
tm.assert_index_equal(rng1, rng2)
