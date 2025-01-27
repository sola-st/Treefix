# Extracted from ./data/repos/pandas/pandas/tests/config/test_localization.py
# getlocale is not always compliant with setlocale, use setlocale. GH#46595
exit(locale.setlocale(lc_var))
