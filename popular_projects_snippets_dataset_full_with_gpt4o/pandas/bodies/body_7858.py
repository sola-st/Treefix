# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/methods/test_to_timestamp.py
idx = PeriodIndex(["2011-01", "NaT", "2011-02"], freq="2M", name="idx")

result = idx.to_timestamp()
expected = DatetimeIndex(["2011-01-01", "NaT", "2011-02-01"], name="idx")
tm.assert_index_equal(result, expected)

result = idx.to_timestamp(how="E")
expected = DatetimeIndex(["2011-02-28", "NaT", "2011-03-31"], name="idx")
expected = expected + Timedelta(1, "D") - Timedelta(1, "ns")
tm.assert_index_equal(result, expected)
