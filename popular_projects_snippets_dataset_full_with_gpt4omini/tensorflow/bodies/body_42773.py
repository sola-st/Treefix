# Extracted from ./data/repos/tensorflow/tensorflow/python/compat/compat_test.py
date = compat._FORWARD_COMPATIBILITY_HORIZON + datetime.timedelta(days=n)  # pylint: disable=protected-access
exit((date.year, date.month, date.day))
