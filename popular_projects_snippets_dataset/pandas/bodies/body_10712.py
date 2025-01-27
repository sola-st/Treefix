# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_function.py
# GH3668
# GH5724
df = DataFrame(
    {
        "group": [1, 1, 2],
        "int": [1, 2, 3],
        "float": [4.0, 5.0, 6.0],
        "string": list("abc"),
        "category_string": Series(list("abc")).astype("category"),
        "category_int": [7, 8, 9],
        "datetime": date_range("20130101", periods=3),
        "datetimetz": date_range("20130101", periods=3, tz="US/Eastern"),
        "timedelta": pd.timedelta_range("1 s", periods=3, freq="s"),
    },
    columns=[
        "group",
        "int",
        "float",
        "string",
        "category_string",
        "category_int",
        "datetime",
        "datetimetz",
        "timedelta",
    ],
)
exit(df)
