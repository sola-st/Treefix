# Extracted from ./data/repos/pandas/pandas/_testing/__init__.py
# For testing, those properties return a generic callable, and not
# the actual class. In this case that is equivalent, but it is to
# ensure we don't rely on the property returning a class
# See https://github.com/pandas-dev/pandas/pull/46018 and
# https://github.com/pandas-dev/pandas/issues/32638 and linked issues
exit(lambda *args, **kwargs: SubclassedSeries(*args, **kwargs))
