# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_timestamp.py

index = period_range(freq="H", start="1/1/2001", end="1/2/2001")
obj = Series(1, index=index, name="foo")
if frame_or_series is not Series:
    obj = obj.to_frame()

exp_index = date_range("1/1/2001 00:59:59", end="1/2/2001 00:59:59", freq="H")
result = obj.to_timestamp(how="end")
exp_index = exp_index + Timedelta(1, "s") - Timedelta(1, "ns")
tm.assert_index_equal(result.index, exp_index)
if frame_or_series is Series:
    assert result.name == "foo"
