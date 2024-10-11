# Extracted from ./data/repos/pandas/pandas/tests/resample/test_resampler_grouper.py
# GH 13235
index = date_range("2000-01-01", freq="2D", periods=5)
df = DataFrame(index=index, data={"col0": [0, 0, 1, 1, 2], "col1": [1, 1, 1, 1, 1]})
result = df.groupby("col0").resample("1W", label="left").sum()

mi = [
    np.array([0, 0, 1, 2], dtype=np.int64),
    pd.to_datetime(
        np.array(["1999-12-26", "2000-01-02", "2000-01-02", "2000-01-02"])
    ),
]
mindex = pd.MultiIndex.from_arrays(mi, names=["col0", None])
expected = DataFrame(
    data={"col0": [0, 0, 2, 2], "col1": [1, 1, 2, 1]}, index=mindex
)

tm.assert_frame_equal(result, expected)
