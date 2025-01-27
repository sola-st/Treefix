# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_put.py
# GH 7796
# test of PeriodIndex in HDFStore
df = DataFrame(
    np.random.randn(5, 1), index=pd.period_range("20220101", freq="M", periods=5)
)

path = tmp_path / setup_path
df.to_hdf(path, "df", mode="w", format=format)
expected = pd.read_hdf(path, "df")
tm.assert_frame_equal(df, expected)
