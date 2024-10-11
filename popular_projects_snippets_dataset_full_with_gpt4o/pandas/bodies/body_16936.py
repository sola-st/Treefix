# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_append.py
# GH 23682
date = Timestamp("2018-10-24 07:30:00", tz=dateutil.tz.tzutc())
ser = Series({"a": 1.0, "b": 2.0, "date": date})
df = DataFrame(columns=["c", "d"])
result_a = df._append(ser, ignore_index=True)
expected = DataFrame(
    [[np.nan, np.nan, 1.0, 2.0, date]], columns=["c", "d", "a", "b", "date"]
)
# These columns get cast to object after append
expected["c"] = expected["c"].astype(object)
expected["d"] = expected["d"].astype(object)
tm.assert_frame_equal(result_a, expected)

expected = DataFrame(
    [[np.nan, np.nan, 1.0, 2.0, date]] * 2, columns=["c", "d", "a", "b", "date"]
)
expected["c"] = expected["c"].astype(object)
expected["d"] = expected["d"].astype(object)
result_b = result_a._append(ser, ignore_index=True)
tm.assert_frame_equal(result_b, expected)

result = df._append([ser, ser], ignore_index=True)
tm.assert_frame_equal(result, expected)
