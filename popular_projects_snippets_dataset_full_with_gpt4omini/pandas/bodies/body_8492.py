# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_partial_slicing.py
# GH 27516
df = DataFrame({"A": range(24)}, index=date_range("2000", periods=24, freq="M"))
expected = Series(
    range(12), index=date_range("2000", periods=12, freq="M"), name="A"
)
result = df.loc["2000", "A"]
tm.assert_series_equal(result, expected)
