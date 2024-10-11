# Extracted from ./data/repos/pandas/pandas/tests/resample/test_resampler_grouper.py
# GH 42905
ts = Timestamp("2021-02-28 00:00:00")
df = DataFrame({"class": ["beta"], "value": [69]}, index=Index([ts], name="date"))
resampled = df.groupby("class").resample("M")["value"]
result = resampled.agg(["sum", "size"])
expected = DataFrame(
    [[69, 1]],
    index=pd.MultiIndex.from_tuples([("beta", ts)], names=["class", "date"]),
    columns=["sum", "size"],
)
tm.assert_frame_equal(result, expected)
