# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_function.py
# mean / median
expected_columns_numeric = Index(["int", "float", "category_int"])

gb = df.groupby("group")
expected = DataFrame(
    {
        "category_int": [7.5, 9],
        "float": [4.5, 6.0],
        "timedelta": [pd.Timedelta("1.5s"), pd.Timedelta("3s")],
        "int": [1.5, 3],
        "datetime": [
            Timestamp("2013-01-01 12:00:00"),
            Timestamp("2013-01-03 00:00:00"),
        ],
        "datetimetz": [
            Timestamp("2013-01-01 12:00:00", tz="US/Eastern"),
            Timestamp("2013-01-03 00:00:00", tz="US/Eastern"),
        ],
    },
    index=Index([1, 2], name="group"),
    columns=[
        "int",
        "float",
        "category_int",
    ],
)

result = getattr(gb, method)(numeric_only=True)
tm.assert_frame_equal(result.reindex_like(expected), expected)

expected_columns = expected.columns

self._check(df, method, expected_columns, expected_columns_numeric)
