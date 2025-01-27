# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/methods/test_to_timestamp.py
idx = period_range(start="2011", periods=2, freq="1D1H", name="idx")

result = idx.to_timestamp()
expected = DatetimeIndex(["2011-01-01 00:00", "2011-01-02 01:00"], name="idx")
tm.assert_index_equal(result, expected)

result = idx.to_timestamp(how="E")
expected = DatetimeIndex(
    ["2011-01-02 00:59:59", "2011-01-03 01:59:59"], name="idx"
)
expected = expected + Timedelta(1, "s") - Timedelta(1, "ns")
tm.assert_index_equal(result, expected)

result = idx.to_timestamp(how="E", freq="H")
expected = DatetimeIndex(["2011-01-02 00:00", "2011-01-03 01:00"], name="idx")
expected = expected + Timedelta(1, "h") - Timedelta(1, "ns")
tm.assert_index_equal(result, expected)
