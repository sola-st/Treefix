# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
df = DataFrame(data, index=[1, 2], columns=["x", "x"])

result = read_json(
    df.to_json(orient=orient), orient=orient, convert_dates=["x"]
)
if orient == "values":
    expected = DataFrame(data)
    if expected.iloc[:, 0].dtype == "datetime64[ns]":
        # orient == "values" by default will write Timestamp objects out
        # in milliseconds; these are internally stored in nanosecond,
        # so divide to get where we need
        # TODO: a to_epoch method would also solve; see GH 14772
        expected.iloc[:, 0] = expected.iloc[:, 0].view(np.int64) // 1000000
elif orient == "split":
    expected = df
    expected.columns = ["x", "x.1"]

tm.assert_frame_equal(result, expected)
