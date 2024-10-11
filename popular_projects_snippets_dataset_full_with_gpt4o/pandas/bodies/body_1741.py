# Extracted from ./data/repos/pandas/pandas/tests/resample/test_datetime_index.py

# GH 4812
# dup columns with resample raising
df = DataFrame(
    np.random.randn(4, 12),
    index=[2000, 2000, 2000, 2000],
    columns=[Period(year=2000, month=i + 1, freq="M") for i in range(12)],
)
df.iloc[3, :] = np.nan
result = df.resample("Q", axis=1).mean()
expected = df.groupby(lambda x: int((x.month - 1) / 3), axis=1).mean()
expected.columns = [Period(year=2000, quarter=i + 1, freq="Q") for i in range(4)]
tm.assert_frame_equal(result, expected)
