# Extracted from ./data/repos/pandas/pandas/tests/resample/test_resampler_grouper.py

# GH 13174
# multiple calls after selection causing an issue with aliasing
data = [{"id": 1, "buyer": "A"}, {"id": 2, "buyer": "B"}]
df = DataFrame(data, index=date_range("2016-01-01", periods=2))
r = df.groupby("id").resample("1D")
result = r["buyer"].count()
expected = Series(
    [1, 1],
    index=pd.MultiIndex.from_tuples(
        [(1, Timestamp("2016-01-01")), (2, Timestamp("2016-01-02"))],
        names=["id", None],
    ),
    name="buyer",
)
tm.assert_series_equal(result, expected)

result = r["buyer"].count()
tm.assert_series_equal(result, expected)
