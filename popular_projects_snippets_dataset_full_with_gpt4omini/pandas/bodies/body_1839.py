# Extracted from ./data/repos/pandas/pandas/tests/resample/test_resample_api.py

# GH 15021
# .groupby(...).resample(on=...) results in an unexpected
# keyword warning.
df = DataFrame(
    {
        "key": ["A", "B"] * 5,
        "dates": date_range("2016-01-01", periods=10),
        "values": np.random.randn(10),
    }
)

expected = df.set_index("dates").groupby("key").resample("D").mean()
result = df.groupby("key").resample("D", on="dates").mean()
tm.assert_frame_equal(result, expected)
