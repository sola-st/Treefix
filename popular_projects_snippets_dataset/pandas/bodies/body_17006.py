# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_categorical.py
# GH-23816
a = Series(pd.date_range("2017-01-01", periods=2, tz="US/Pacific"))
b = Series(["a", "b"], dtype="category")
result = pd.concat([a, b], ignore_index=True)
expected = Series(
    [
        pd.Timestamp("2017-01-01", tz="US/Pacific"),
        pd.Timestamp("2017-01-02", tz="US/Pacific"),
        "a",
        "b",
    ]
)
tm.assert_series_equal(result, expected)
