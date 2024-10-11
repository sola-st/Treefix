# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_fillna.py
# GH#6587
# make sure that we are treating as integer when filling
ser = Series([NaT, NaT, "2013-08-05 15:30:00.000001"], dtype="M8[ns]")

expected = Series(
    [
        "2013-08-05 15:30:00.000001",
        "2013-08-05 15:30:00.000001",
        "2013-08-05 15:30:00.000001",
    ],
    dtype="M8[ns]",
)
result = ser.fillna(method="backfill")
tm.assert_series_equal(result, expected)
