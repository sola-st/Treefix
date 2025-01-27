# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_astype.py
# str formatting
result = timezone_frame.astype(str)
expected = DataFrame(
    [
        [
            "2013-01-01",
            "2013-01-01 00:00:00-05:00",
            "2013-01-01 00:00:00+01:00",
        ],
        ["2013-01-02", "NaT", "NaT"],
        [
            "2013-01-03",
            "2013-01-03 00:00:00-05:00",
            "2013-01-03 00:00:00+01:00",
        ],
    ],
    columns=timezone_frame.columns,
)
tm.assert_frame_equal(result, expected)

with option_context("display.max_columns", 20):
    result = str(timezone_frame)
    assert (
        "0 2013-01-01 2013-01-01 00:00:00-05:00 2013-01-01 00:00:00+01:00"
    ) in result
    assert (
        "1 2013-01-02                       NaT                       NaT"
    ) in result
    assert (
        "2 2013-01-03 2013-01-03 00:00:00-05:00 2013-01-03 00:00:00+01:00"
    ) in result
