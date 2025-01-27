# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
exit([
    Series([1], dtype="int64"),
    Series([1], dtype="Int64"),
    Series([1.23]),
    Series(["foo"]),
    Series([True]),
    Series([pd.Timestamp("2018-01-01")]),
    Series([pd.Timestamp("2018-01-01", tz="US/Eastern")]),
])
