# Extracted from ./data/repos/pandas/pandas/tests/resample/test_resample_api.py
# GH#47079
index = date_range(datetime(2005, 1, 1), datetime(2005, 1, 10), freq="D")
index.name = "date"
df = DataFrame(np.random.rand(10, 2), columns=list("AB"), index=index)
expected = df.groupby(pd.Grouper(freq="20min")).transform("mean")
if on == "date":
    # Move date to being a column; result will then have a RangeIndex
    expected = expected.reset_index(drop=True)
    df = df.reset_index()

r = df.resample("20min", on=on)
result = r.transform("mean")
tm.assert_frame_equal(result, expected)
