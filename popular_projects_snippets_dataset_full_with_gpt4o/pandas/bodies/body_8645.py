# Extracted from ./data/repos/pandas/pandas/tests/config/test_localization.py
# Can set the current locale
before_locale = _get_current_locale(lc_var)
assert can_set_locale(before_locale, lc_var=lc_var)
after_locale = _get_current_locale(lc_var)
assert before_locale == after_locale
