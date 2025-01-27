# Extracted from ./data/repos/pandas/pandas/tests/strings/test_case_justify.py
s = Series(["a", np.nan, "b", True, datetime.today(), "c", "eee", None, 1, 2.0])

result = s.str.center(5)
expected = Series(
    [
        "  a  ",
        np.nan,
        "  b  ",
        np.nan,
        np.nan,
        "  c  ",
        " eee ",
        np.nan,
        np.nan,
        np.nan,
    ]
)
tm.assert_series_equal(result, expected)

result = s.str.ljust(5)
expected = Series(
    [
        "a    ",
        np.nan,
        "b    ",
        np.nan,
        np.nan,
        "c    ",
        "eee  ",
        np.nan,
        np.nan,
        np.nan,
    ]
)
tm.assert_series_equal(result, expected)

result = s.str.rjust(5)
expected = Series(
    [
        "    a",
        np.nan,
        "    b",
        np.nan,
        np.nan,
        "    c",
        "  eee",
        np.nan,
        np.nan,
        np.nan,
    ]
)
tm.assert_series_equal(result, expected)
