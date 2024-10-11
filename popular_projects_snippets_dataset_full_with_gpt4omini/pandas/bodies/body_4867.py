# Extracted from ./data/repos/pandas/pandas/tests/strings/test_find_replace.py
mixed = Series(
    np.array(
        ["a", np.nan, "b", True, datetime.today(), "foo", None, 1, 2.0],
        dtype=object,
    )
)
result = mixed.str.contains("o")
expected = Series(
    np.array(
        [False, np.nan, False, np.nan, np.nan, True, np.nan, np.nan, np.nan],
        dtype=np.object_,
    )
)
tm.assert_series_equal(result, expected)
