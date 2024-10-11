# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_boxplot_method.py
# GH 22799
df = DataFrame(
    {
        "a": date_range("2012-01-01", periods=100),
        "b": np.random.randn(100),
        "c": np.random.randn(100) + 2,
        "d": date_range("2012-01-01", periods=100).astype(str),
        "e": date_range("2012-01-01", periods=100, tz="UTC"),
        "f": timedelta_range("1 days", periods=100),
    }
)
ax = df.plot(kind="box")
assert [x.get_text() for x in ax.get_xticklabels()] == ["b", "c"]
