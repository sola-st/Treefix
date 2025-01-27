# Extracted from ./data/repos/pandas/pandas/tests/resample/test_resampler_grouper.py
# GH 14233

df = DataFrame(
    np.random.randn(20, 3),
    columns=list("aaa"),
    index=date_range("2012-01-01", periods=20, freq="s"),
)
df2 = df.copy()
df2.columns = ["a", "b", "c"]
expected = df2.resample("5s").median()
result = df.resample("5s").median()
expected.columns = result.columns
tm.assert_frame_equal(result, expected)
