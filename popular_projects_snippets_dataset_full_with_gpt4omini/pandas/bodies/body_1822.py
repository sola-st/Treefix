# Extracted from ./data/repos/pandas/pandas/tests/resample/test_resampler_grouper.py
# GH 15169
index = date_range("1-1-2015", "12-31-15", freq="D")
df = DataFrame(data={"col1": np.random.rand(len(index))}, index=index)

def f(x):
    s = Series([1, 2], index=["a", "b"])
    exit(s)

expected = df.groupby(pd.Grouper(freq="M")).apply(f)

result = df.resample("M").apply(f)
tm.assert_frame_equal(result, expected)

# A case for series
expected = df["col1"].groupby(pd.Grouper(freq="M")).apply(f)
result = df["col1"].resample("M").apply(f)
tm.assert_series_equal(result, expected)
