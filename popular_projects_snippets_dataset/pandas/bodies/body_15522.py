# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_drop_duplicates.py
# GH#44351
ser = Series(
    Categorical(
        [True, False, True, False, nulls_fixture],
        categories=[True, False],
        ordered=True,
    )
)
result = ser.drop_duplicates()
expected = Series(
    Categorical([True, False, np.nan], categories=[True, False], ordered=True),
    index=[0, 1, 4],
)
tm.assert_series_equal(result, expected)
