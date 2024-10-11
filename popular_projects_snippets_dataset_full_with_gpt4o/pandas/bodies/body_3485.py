# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_quantile.py
# DatetimeLikeBlock may be consolidated and contain NaT in different loc
df = DataFrame(
    {
        "A": [
            Timestamp("2011-01-01"),
            pd.NaT,
            Timestamp("2011-01-02"),
            Timestamp("2011-01-03"),
        ],
        "a": [
            Timestamp("2011-01-01"),
            Timestamp("2011-01-02"),
            pd.NaT,
            Timestamp("2011-01-03"),
        ],
        "B": [
            Timestamp("2011-01-01", tz="US/Eastern"),
            pd.NaT,
            Timestamp("2011-01-02", tz="US/Eastern"),
            Timestamp("2011-01-03", tz="US/Eastern"),
        ],
        "b": [
            Timestamp("2011-01-01", tz="US/Eastern"),
            Timestamp("2011-01-02", tz="US/Eastern"),
            pd.NaT,
            Timestamp("2011-01-03", tz="US/Eastern"),
        ],
        "C": [
            pd.Timedelta("1 days"),
            pd.Timedelta("2 days"),
            pd.Timedelta("3 days"),
            pd.NaT,
        ],
        "c": [
            pd.NaT,
            pd.Timedelta("1 days"),
            pd.Timedelta("2 days"),
            pd.Timedelta("3 days"),
        ],
    },
    columns=list("AaBbCc"),
)

res = df.quantile(0.5, numeric_only=False)
exp = Series(
    [
        Timestamp("2011-01-02"),
        Timestamp("2011-01-02"),
        Timestamp("2011-01-02", tz="US/Eastern"),
        Timestamp("2011-01-02", tz="US/Eastern"),
        pd.Timedelta("2 days"),
        pd.Timedelta("2 days"),
    ],
    name=0.5,
    index=list("AaBbCc"),
)
tm.assert_series_equal(res, exp)

res = df.quantile([0.5], numeric_only=False)
exp = DataFrame(
    [
        [
            Timestamp("2011-01-02"),
            Timestamp("2011-01-02"),
            Timestamp("2011-01-02", tz="US/Eastern"),
            Timestamp("2011-01-02", tz="US/Eastern"),
            pd.Timedelta("2 days"),
            pd.Timedelta("2 days"),
        ]
    ],
    index=[0.5],
    columns=list("AaBbCc"),
)
tm.assert_frame_equal(res, exp)
