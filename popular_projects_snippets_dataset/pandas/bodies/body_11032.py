# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply.py
# GH 14849
data = DataFrame.from_records(
    [
        (pd.Timestamp(2016, 1, 1), "red", "dark", 1, "8"),
        (pd.Timestamp(2015, 1, 1), "green", "stormy", 2, "9"),
        (pd.Timestamp(2014, 1, 1), "blue", "bright", 3, "10"),
        (pd.Timestamp(2013, 1, 1), "blue", "calm", 4, "potato"),
    ],
    columns=["observation", "color", "mood", "intensity", "score"],
)
result = data.groupby("color").apply(lambda g: g.iloc[0]).dtypes
expected = Series(
    [np.dtype("datetime64[ns]"), object, object, np.int64, object],
    index=["observation", "color", "mood", "intensity", "score"],
)
tm.assert_series_equal(result, expected)
