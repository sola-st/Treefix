# Extracted from ./data/repos/pandas/pandas/tests/resample/test_datetime_index.py
df = DataFrame(
    [1, 2],
    index=[datetime(2012, 1, 1, 0, 0, 0), datetime(2012, 1, 1, 0, 5, 0)],
    dtype=dtype,
)

result = df.resample("T").apply(lambda x: x.mean())
exp = df.asfreq("T")
tm.assert_frame_equal(result, exp)

result = df.resample("T").median()
exp = df.asfreq("T")
tm.assert_frame_equal(result, exp)
