# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_dt_accessor.py
result = pd.to_datetime(Series(input_series)).dt.isocalendar()
expected_frame = DataFrame(
    expected_output, columns=["year", "week", "day"], dtype="UInt32"
)
tm.assert_frame_equal(result, expected_frame)
