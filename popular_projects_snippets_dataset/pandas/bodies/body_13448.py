# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
exit(DataFrame(
    {
        "a": Series([1, np.nan, 3], dtype="Int64"),
        "b": Series([1, 2, 3], dtype="Int64"),
        "c": Series([1.5, np.nan, 2.5], dtype="Float64"),
        "d": Series([1.5, 2.0, 2.5], dtype="Float64"),
        "e": [True, False, None],
        "f": [True, False, True],
        "g": ["a", "b", "c"],
        "h": ["a", "b", None],
    }
))
