# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# see gh-8260
us_eastern = pytz.timezone("US/Eastern")
arr = np.array(
    [
        us_eastern.localize(
            datetime(year=2000, month=1, day=1, hour=3, minute=0)
        ),
        us_eastern.localize(
            datetime(year=2000, month=6, day=1, hour=3, minute=0)
        ),
    ],
    dtype=object,
)
result = to_datetime(arr, utc=True, cache=cache)
expected = DatetimeIndex(
    ["2000-01-01 08:00:00+00:00", "2000-06-01 07:00:00+00:00"],
    dtype="datetime64[ns, UTC]",
    freq=None,
)
tm.assert_index_equal(result, expected)
