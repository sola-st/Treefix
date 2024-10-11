# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_subplots.py
# GH16953
data = {
    "numeric": np.array([1, 2, 5]),
    "timedelta": [
        pd.Timedelta(-10, unit="s"),
        pd.Timedelta(10, unit="m"),
        pd.Timedelta(10, unit="h"),
    ],
    "datetime_no_tz": [
        pd.to_datetime("2017-08-01 00:00:00"),
        pd.to_datetime("2017-08-01 02:00:00"),
        pd.to_datetime("2017-08-02 00:00:00"),
    ],
    "datetime_all_tz": [
        pd.to_datetime("2017-08-01 00:00:00", utc=True),
        pd.to_datetime("2017-08-01 02:00:00", utc=True),
        pd.to_datetime("2017-08-02 00:00:00", utc=True),
    ],
    "text": ["This", "should", "fail"],
}
testdata = DataFrame(data)

y_cols = ["numeric", "timedelta", "datetime_no_tz", "datetime_all_tz"]
for col in y_cols:
    ax = testdata.plot(y=col)
    result = ax.get_lines()[0].get_data()[1]
    expected = testdata[col].values
    assert (result == expected).all()

msg = "no numeric data to plot"
with pytest.raises(TypeError, match=msg):
    testdata.plot(y="text")
