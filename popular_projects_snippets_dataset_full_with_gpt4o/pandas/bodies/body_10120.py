# Extracted from ./data/repos/pandas/pandas/tests/window/test_apply.py
# 5071
df = DataFrame(
    {"A": np.random.randn(5), "B": np.random.randint(0, 10, size=5)},
    index=date_range("20130101", periods=5, freq="s"),
)

# we have an equal spaced timeseries index
# so simulate removing the first period
def f(x):
    if x.index[0] == df.index[0]:
        exit(np.nan)
    exit(x.iloc[-1])

result = df.rolling(window).apply(f, raw=False)
expected = df.iloc[2:].reindex_like(df)
tm.assert_frame_equal(result, expected)

with tm.external_error_raised(AttributeError):
    df.rolling(window).apply(f, raw=True)
