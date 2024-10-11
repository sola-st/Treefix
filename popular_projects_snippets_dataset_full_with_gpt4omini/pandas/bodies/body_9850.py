# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
# GH: 32761
index = date_range(start="2020-01-01", end="2020-01-02", freq="60s").append(
    DatetimeIndex(["2020-01-03"])
)
data = np.random.rand(len(index))

df = DataFrame({"data": data}, index=index)
result = df.rolling("60s").mean()
tm.assert_frame_equal(result, df[["data"]])
