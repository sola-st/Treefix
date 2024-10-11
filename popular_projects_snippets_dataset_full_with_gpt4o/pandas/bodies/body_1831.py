# Extracted from ./data/repos/pandas/pandas/tests/resample/test_resampler_grouper.py
# https://github.com/pandas-dev/pandas/issues/39329

dates = date_range("2020-01-01", periods=15, freq="D")
df1 = DataFrame({"key": "A", "date": dates, "col1": range(15), "col_object": "val"})
df2 = DataFrame({"key": "B", "date": dates, "col1": range(15)})
df = pd.concat([df1, df2], ignore_index=True)
if consolidate:
    df = df._consolidate()

result = df.groupby(["key"]).resample("W", on="date").min()
idx = pd.MultiIndex.from_arrays(
    [
        ["A"] * 3 + ["B"] * 3,
        pd.to_datetime(["2020-01-05", "2020-01-12", "2020-01-19"] * 2),
    ],
    names=["key", "date"],
)
expected = DataFrame(
    {
        "key": ["A"] * 3 + ["B"] * 3,
        "col1": [0, 5, 12] * 2,
        "col_object": ["val"] * 3 + [np.nan] * 3,
    },
    index=idx,
)
tm.assert_frame_equal(result, expected)
