# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_timestamp.py
K = 5
index = period_range(freq="A", start="1/1/2001", end="12/1/2009")
df = DataFrame(
    np.random.randn(len(index), K),
    index=index,
    columns=["A", "B", "C", "D", "E"],
)
df["mix"] = "a"

# columns
df = df.T

exp_index = date_range("1/1/2001", end="12/31/2009", freq="A-DEC")
exp_index = exp_index + Timedelta(1, "D") - Timedelta(1, "ns")
result = df.to_timestamp("D", "end", axis=1)
tm.assert_index_equal(result.columns, exp_index)
tm.assert_numpy_array_equal(result.values, df.values)

exp_index = date_range("1/1/2001", end="1/1/2009", freq="AS-JAN")
result = df.to_timestamp("D", "start", axis=1)
tm.assert_index_equal(result.columns, exp_index)

delta = timedelta(hours=23)
result = df.to_timestamp("H", "end", axis=1)
exp_index = _get_with_delta(delta)
exp_index = exp_index + Timedelta(1, "h") - Timedelta(1, "ns")
tm.assert_index_equal(result.columns, exp_index)

delta = timedelta(hours=23, minutes=59)
result = df.to_timestamp("T", "end", axis=1)
exp_index = _get_with_delta(delta)
exp_index = exp_index + Timedelta(1, "m") - Timedelta(1, "ns")
tm.assert_index_equal(result.columns, exp_index)

result = df.to_timestamp("S", "end", axis=1)
delta = timedelta(hours=23, minutes=59, seconds=59)
exp_index = _get_with_delta(delta)
exp_index = exp_index + Timedelta(1, "s") - Timedelta(1, "ns")
tm.assert_index_equal(result.columns, exp_index)

result1 = df.to_timestamp("5t", axis=1)
result2 = df.to_timestamp("t", axis=1)
expected = date_range("2001-01-01", "2009-01-01", freq="AS")
assert isinstance(result1.columns, DatetimeIndex)
assert isinstance(result2.columns, DatetimeIndex)
tm.assert_numpy_array_equal(result1.columns.asi8, expected.asi8)
tm.assert_numpy_array_equal(result2.columns.asi8, expected.asi8)
# PeriodIndex.to_timestamp always use 'infer'
assert result1.columns.freqstr == "AS-JAN"
assert result2.columns.freqstr == "AS-JAN"
