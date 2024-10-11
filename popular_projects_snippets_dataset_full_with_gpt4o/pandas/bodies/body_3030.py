# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_timestamp.py
K = 5
index = period_range(freq="A", start="1/1/2001", end="12/1/2009")
obj = DataFrame(
    np.random.randn(len(index), K),
    index=index,
    columns=["A", "B", "C", "D", "E"],
)
obj["mix"] = "a"
obj = tm.get_obj(obj, frame_or_series)

exp_index = date_range("1/1/2001", end="12/31/2009", freq="A-DEC")
exp_index = exp_index + Timedelta(1, "D") - Timedelta(1, "ns")
result = obj.to_timestamp("D", "end")
tm.assert_index_equal(result.index, exp_index)
tm.assert_numpy_array_equal(result.values, obj.values)
if frame_or_series is Series:
    assert result.name == "A"

exp_index = date_range("1/1/2001", end="1/1/2009", freq="AS-JAN")
result = obj.to_timestamp("D", "start")
tm.assert_index_equal(result.index, exp_index)

result = obj.to_timestamp(how="start")
tm.assert_index_equal(result.index, exp_index)

delta = timedelta(hours=23)
result = obj.to_timestamp("H", "end")
exp_index = _get_with_delta(delta)
exp_index = exp_index + Timedelta(1, "h") - Timedelta(1, "ns")
tm.assert_index_equal(result.index, exp_index)

delta = timedelta(hours=23, minutes=59)
result = obj.to_timestamp("T", "end")
exp_index = _get_with_delta(delta)
exp_index = exp_index + Timedelta(1, "m") - Timedelta(1, "ns")
tm.assert_index_equal(result.index, exp_index)

result = obj.to_timestamp("S", "end")
delta = timedelta(hours=23, minutes=59, seconds=59)
exp_index = _get_with_delta(delta)
exp_index = exp_index + Timedelta(1, "s") - Timedelta(1, "ns")
tm.assert_index_equal(result.index, exp_index)
