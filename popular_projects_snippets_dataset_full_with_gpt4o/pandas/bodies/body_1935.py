# Extracted from ./data/repos/pandas/pandas/tests/resample/test_timedelta.py
# GH 13022
index = timedelta_range("00:00:00", "00:10:00", freq="5T")
df = DataFrame(data={"value": [1, 5, 10]}, index=index)
result = df.resample("2T").asfreq()
expected_data = {"value": [1, np.nan, np.nan, np.nan, np.nan, 10]}
expected = DataFrame(
    data=expected_data, index=timedelta_range("00:00:00", "00:10:00", freq="2T")
)
tm.assert_frame_equal(result, expected)
