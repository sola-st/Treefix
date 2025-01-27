# Extracted from ./data/repos/pandas/pandas/tests/strings/test_find_replace.py
mixed = Series(
    [
        "aBAD_BAD",
        np.nan,
        "BAD_b_BAD",
        True,
        datetime.today(),
        "foo",
        None,
        1,
        2.0,
    ]
)
result = Series(mixed).str.match(".*(BAD[_]+).*(BAD)")
expected = Series(
    [True, np.nan, True, np.nan, np.nan, False, np.nan, np.nan, np.nan]
)
assert isinstance(result, Series)
tm.assert_series_equal(result, expected)
