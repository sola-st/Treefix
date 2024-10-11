# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_asof.py
# we specialize by type, so test that this is correct
df1 = pd.DataFrame(
    {
        "time": to_datetime(
            [
                "20160525 13:30:00.020",
                "20160525 13:30:00.030",
                "20160525 13:30:00.040",
                "20160525 13:30:00.050",
                "20160525 13:30:00.060",
            ]
        ),
        "key": [1, 2, 1, 3, 2],
        "value1": [1.1, 1.2, 1.3, 1.4, 1.5],
    },
    columns=["time", "key", "value1"],
)

df2 = pd.DataFrame(
    {
        "time": to_datetime(
            [
                "20160525 13:30:00.015",
                "20160525 13:30:00.020",
                "20160525 13:30:00.025",
                "20160525 13:30:00.035",
                "20160525 13:30:00.040",
                "20160525 13:30:00.055",
                "20160525 13:30:00.060",
                "20160525 13:30:00.065",
            ]
        ),
        "key": [2, 1, 1, 3, 2, 1, 2, 3],
        "value2": [2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8],
    },
    columns=["time", "key", "value2"],
)

result = merge_asof(df1, df2, on="time", by="key")

expected = pd.DataFrame(
    {
        "time": to_datetime(
            [
                "20160525 13:30:00.020",
                "20160525 13:30:00.030",
                "20160525 13:30:00.040",
                "20160525 13:30:00.050",
                "20160525 13:30:00.060",
            ]
        ),
        "key": [1, 2, 1, 3, 2],
        "value1": [1.1, 1.2, 1.3, 1.4, 1.5],
        "value2": [2.2, 2.1, 2.3, 2.4, 2.7],
    },
    columns=["time", "key", "value1", "value2"],
)

tm.assert_frame_equal(result, expected)
