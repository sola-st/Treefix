# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_duplicates.py
# GH 17927
expected = Series(
    [False, False, False, True, False, False, False, True, False, True],
    dtype=bool,
)
result = Series(
    [
        np.nan + np.nan * 1j,
        0,
        1j,
        1j,
        1,
        1 + 1j,
        1 + 2j,
        1 + 1j,
        np.nan,
        np.nan + np.nan * 1j,
    ],
    dtype=dtype,
).duplicated()
tm.assert_series_equal(result, expected)
