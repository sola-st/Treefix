# Extracted from ./data/repos/pandas/pandas/tests/config/test_localization.py
# Cannot set an invalid locale.
before_locale = _get_current_locale(lc_var)
assert not can_set_locale("non-existent_locale", lc_var=lc_var)
after_locale = _get_current_locale(lc_var)
assert before_locale == after_locale
