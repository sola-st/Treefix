# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_json_table_schema.py
exit(DataFrame(
    {
        "A": [1, 2, 3, 4],
        "B": ["a", "b", "c", "c"],
        "C": pd.date_range("2016-01-01", freq="d", periods=4),
        "D": pd.timedelta_range("1H", periods=4, freq="T"),
        "E": pd.Series(pd.Categorical(["a", "b", "c", "c"])),
        "F": pd.Series(pd.Categorical(["a", "b", "c", "c"], ordered=True)),
        "G": [1.0, 2.0, 3, 4.0],
        "H": pd.date_range("2016-01-01", freq="d", periods=4, tz="US/Central"),
    },
    index=pd.Index(range(4), name="idx"),
))
