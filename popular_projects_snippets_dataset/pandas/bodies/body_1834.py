# Extracted from ./data/repos/pandas/pandas/tests/resample/test_resampler_grouper.py
# GH 46826
df = DataFrame(
    {"A": [1] * 3 + [2] * 3 + [1] * 3 + [2] * 3, "B": np.arange(12)},
    index=date_range("31/12/2000 18:00", freq="H", periods=12),
)
result = df.groupby("A").resample("D").size()
expected = Series(
    3,
    index=pd.MultiIndex.from_tuples(
        [
            (1, Timestamp("2000-12-31")),
            (1, Timestamp("2001-01-01")),
            (2, Timestamp("2000-12-31")),
            (2, Timestamp("2001-01-01")),
        ],
        names=["A", None],
    ),
)
tm.assert_series_equal(result, expected)
