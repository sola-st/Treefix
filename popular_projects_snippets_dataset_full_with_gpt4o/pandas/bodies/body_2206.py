# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
format_for_string_of_nans = tools._guess_datetime_format_for_array(
    np.array([np.nan, np.nan, np.nan], dtype="O")
)
assert format_for_string_of_nans is None
