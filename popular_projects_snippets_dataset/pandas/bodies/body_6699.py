# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval_range.py
# float value for periods
expected = interval_range(start=0, periods=10)
result = interval_range(start=0, periods=10.5)
tm.assert_index_equal(result, expected)

# equivalent timestamp-like start/end
start, end = Timestamp("2017-01-01"), Timestamp("2017-01-15")
expected = interval_range(start=start, end=end)

result = interval_range(start=start.to_pydatetime(), end=end.to_pydatetime())
tm.assert_index_equal(result, expected)

result = interval_range(start=start.asm8, end=end.asm8)
tm.assert_index_equal(result, expected)

# equivalent freq with timestamp
equiv_freq = [
    "D",
    Day(),
    Timedelta(days=1),
    timedelta(days=1),
    DateOffset(days=1),
]
for freq in equiv_freq:
    result = interval_range(start=start, end=end, freq=freq)
    tm.assert_index_equal(result, expected)

# equivalent timedelta-like start/end
start, end = Timedelta(days=1), Timedelta(days=10)
expected = interval_range(start=start, end=end)

result = interval_range(start=start.to_pytimedelta(), end=end.to_pytimedelta())
tm.assert_index_equal(result, expected)

result = interval_range(start=start.asm8, end=end.asm8)
tm.assert_index_equal(result, expected)

# equivalent freq with timedelta
equiv_freq = ["D", Day(), Timedelta(days=1), timedelta(days=1)]
for freq in equiv_freq:
    result = interval_range(start=start, end=end, freq=freq)
    tm.assert_index_equal(result, expected)
