# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_datetimes.py
# GH 9188
result = concat(
    [DataFrame(date_range("2000", periods=1, tz="UTC")), DataFrame()]
)
expected = DataFrame(date_range("2000", periods=1, tz="UTC"))
tm.assert_frame_equal(result, expected)
