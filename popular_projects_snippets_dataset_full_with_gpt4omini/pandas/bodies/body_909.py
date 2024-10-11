# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_at.py
df = DataFrame(
    data=[[1] * 2], index=DatetimeIndex(data=["2019-01-01", "2019-01-02"])
)
expected = DataFrame(
    data=[[0.5, 1], [1.0, 1]],
    index=DatetimeIndex(data=["2019-01-01", "2019-01-02"]),
)

df.at[row, 0] = 0.5
tm.assert_frame_equal(df, expected)
