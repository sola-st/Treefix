# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
# we *can* concatenate DTI with different freqs.
a = DatetimeArray(pd.date_range("2000", periods=2, freq="D", tz="US/Central"))
b = DatetimeArray(pd.date_range("2000", periods=2, freq="H", tz="US/Central"))
result = DatetimeArray._concat_same_type([a, b])
expected = DatetimeArray(
    pd.to_datetime(
        [
            "2000-01-01 00:00:00",
            "2000-01-02 00:00:00",
            "2000-01-01 00:00:00",
            "2000-01-01 01:00:00",
        ]
    ).tz_localize("US/Central")
)

tm.assert_datetime_array_equal(result, expected)
