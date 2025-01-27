# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py

expected = Series(
    [pd.Timedelta(x, unit=units) + epoch_1960 for x in units_from_epochs]
)

result = Series(to_datetime(units_from_epochs, unit=units, origin=epochs))
tm.assert_series_equal(result, expected)
