# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_dt_accessor.py
# Test Monday -> Sunday and January -> December, in that sequence
if time_locale is None:
    # If the time_locale is None, day-name and month_name should
    # return the english attributes
    expected_days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    expected_months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
else:
    with tm.set_locale(time_locale, locale.LC_TIME):
        expected_days = calendar.day_name[:]
        expected_months = calendar.month_name[1:]

ser = Series(date_range(freq="D", start=datetime(1998, 1, 1), periods=365))
english_days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]
for day, name, eng_name in zip(range(4, 11), expected_days, english_days):
    name = name.capitalize()
    assert ser.dt.day_name(locale=time_locale)[day] == name
    assert ser.dt.day_name(locale=None)[day] == eng_name
ser = pd.concat([ser, Series([pd.NaT])])
assert np.isnan(ser.dt.day_name(locale=time_locale).iloc[-1])

ser = Series(date_range(freq="M", start="2012", end="2013"))
result = ser.dt.month_name(locale=time_locale)
expected = Series([month.capitalize() for month in expected_months])

# work around https://github.com/pandas-dev/pandas/issues/22342
result = result.str.normalize("NFD")
expected = expected.str.normalize("NFD")

tm.assert_series_equal(result, expected)

for s_date, expected in zip(ser, expected_months):
    result = s_date.month_name(locale=time_locale)
    expected = expected.capitalize()

    result = unicodedata.normalize("NFD", result)
    expected = unicodedata.normalize("NFD", expected)

    assert result == expected

ser = pd.concat([ser, Series([pd.NaT])])
assert np.isnan(ser.dt.month_name(locale=time_locale).iloc[-1])
