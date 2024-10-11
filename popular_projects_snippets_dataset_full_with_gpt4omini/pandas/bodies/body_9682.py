# Extracted from ./data/repos/pandas/pandas/tests/arrays/datetimes/test_cumulative.py
# GH#50297
arr = DatetimeArray._from_sequence_not_strict(
    [
        "2000-01-01",
        "2000-01-02",
        "2000-01-03",
    ],
    freq="D",
)
result = arr._accumulate("cummin")
expected = DatetimeArray._from_sequence_not_strict(
    ["2000-01-01"] * 3, freq=None
)
tm.assert_datetime_array_equal(result, expected)

result = arr._accumulate("cummax")
expected = DatetimeArray._from_sequence_not_strict(
    [
        "2000-01-01",
        "2000-01-02",
        "2000-01-03",
    ],
    freq=None,
)
tm.assert_datetime_array_equal(result, expected)
