# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/methods/test_to_timestamp.py
# GH#7228
index = PeriodIndex(["NaT", "2011-01", "2011-02"], freq="M", name="idx")

result = index.to_timestamp("D")
expected = DatetimeIndex(
    [NaT, datetime(2011, 1, 1), datetime(2011, 2, 1)], name="idx"
)
tm.assert_index_equal(result, expected)
assert result.name == "idx"

result2 = result.to_period(freq="M")
tm.assert_index_equal(result2, index)
assert result2.name == "idx"

result3 = result.to_period(freq="3M")
exp = PeriodIndex(["NaT", "2011-01", "2011-02"], freq="3M", name="idx")
tm.assert_index_equal(result3, exp)
assert result3.freqstr == "3M"

msg = "Frequency must be positive, because it represents span: -2A"
with pytest.raises(ValueError, match=msg):
    result.to_period(freq="-2A")
