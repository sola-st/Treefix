# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_duplicated.py
# GH#44351
ser = Series(
    Categorical(
        [True, False, True, False, nulls_fixture],
        categories=[True, False],
        ordered=True,
    )
)
result = ser.duplicated()
expected = Series([False, False, True, True, False])
tm.assert_series_equal(result, expected)
