# Extracted from ./data/repos/pandas/pandas/tests/resample/test_timedelta.py
# GH 10603
df = DataFrame(
    np.random.normal(size=(10000, 4)),
    index=timedelta_range(start="0s", periods=10000, freq="3906250n"),
)
if duplicates:
    # case with non-unique columns
    df.columns = ["A", "B", "A", "C"]

result = df.loc["1s":, :].resample("3s").apply(lambda x: len(x))

expected = DataFrame(
    [[768] * 4] * 12 + [[528] * 4],
    index=timedelta_range(start="1s", periods=13, freq="3s"),
)
expected.columns = df.columns
tm.assert_frame_equal(result, expected)
