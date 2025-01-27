# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
# GH 17354
# Test .day_name(), .month_name
if time_locale is None:
    expected_day = "Monday"
    expected_month = "August"
else:
    with tm.set_locale(time_locale, locale.LC_TIME):
        expected_day = calendar.day_name[0].capitalize()
        expected_month = calendar.month_name[8].capitalize()

result_day = data.day_name(time_locale)
result_month = data.month_name(time_locale)

# Work around https://github.com/pandas-dev/pandas/issues/22342
# different normalizations
expected_day = unicodedata.normalize("NFD", expected_day)
expected_month = unicodedata.normalize("NFD", expected_month)

result_day = unicodedata.normalize("NFD", result_day)
result_month = unicodedata.normalize("NFD", result_month)

assert result_day == expected_day
assert result_month == expected_month

# Test NaT
nan_ts = Timestamp(NaT)
assert np.isnan(nan_ts.day_name(time_locale))
assert np.isnan(nan_ts.month_name(time_locale))
