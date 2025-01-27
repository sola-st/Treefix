# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
frame = DataFrame(
    {
        "a": [timedelta(days=23), timedelta(seconds=5)],
        "b": [1, 2],
        "c": pd.date_range(start="20130101", periods=2),
    }
)

result = read_json(frame.to_json(date_unit="ns"))
result["a"] = pd.to_timedelta(result.a, unit="ns")
result["c"] = pd.to_datetime(result.c)
tm.assert_frame_equal(frame, result)
