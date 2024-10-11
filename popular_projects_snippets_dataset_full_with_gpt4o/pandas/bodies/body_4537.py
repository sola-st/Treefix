# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH19157
dr = date_range(start="20130101T10:00:00", periods=3, freq="T", tz="US/Eastern")
result = DataFrame(dr, columns=["timestamps"])
expected = DataFrame(
    {
        "timestamps": [
            Timestamp("20130101T10:00:00", tz="US/Eastern"),
            Timestamp("20130101T10:01:00", tz="US/Eastern"),
            Timestamp("20130101T10:02:00", tz="US/Eastern"),
        ]
    }
)
tm.assert_frame_equal(result, expected)
