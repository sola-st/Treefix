# Extracted from ./data/repos/pandas/pandas/tests/generic/test_frame.py
# resample
df = DataFrame(
    np.random.randn(1000, 2),
    index=date_range("20130101", periods=1000, freq="s"),
)
result = df.resample("1T")
tm.assert_metadata_equivalent(df, result)
