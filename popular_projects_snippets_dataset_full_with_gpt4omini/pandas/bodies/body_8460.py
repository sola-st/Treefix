# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_misc.py
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

        # GH#11128
dti = date_range(freq="D", start=datetime(1998, 1, 1), periods=365)
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
    assert dti.day_name(locale=time_locale)[day] == name
    assert dti.day_name(locale=None)[day] == eng_name
    ts = Timestamp(datetime(2016, 4, day))
    assert ts.day_name(locale=time_locale) == name
dti = dti.append(DatetimeIndex([pd.NaT]))
assert np.isnan(dti.day_name(locale=time_locale)[-1])
ts = Timestamp(pd.NaT)
assert np.isnan(ts.day_name(locale=time_locale))

# GH#12805
dti = date_range(freq="M", start="2012", end="2013")
result = dti.month_name(locale=time_locale)
expected = Index([month.capitalize() for month in expected_months])

# work around different normalization schemes
# https://github.com/pandas-dev/pandas/issues/22342
result = result.str.normalize("NFD")
expected = expected.str.normalize("NFD")

tm.assert_index_equal(result, expected)

for date, expected in zip(dti, expected_months):
    result = date.month_name(locale=time_locale)
    expected = expected.capitalize()

    result = unicodedata.normalize("NFD", result)
    expected = unicodedata.normalize("NFD", result)

    assert result == expected
dti = dti.append(DatetimeIndex([pd.NaT]))
assert np.isnan(dti.month_name(locale=time_locale)[-1])
