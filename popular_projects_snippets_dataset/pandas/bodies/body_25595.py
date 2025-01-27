# Extracted from ./data/repos/pandas/pandas/util/_decorators.py
func.__doc__ = func.__doc__ if func.__doc__ else ""
self.addendum = self.addendum if self.addendum else ""
docitems = [func.__doc__, self.addendum]
func.__doc__ = dedent(self.join.join(docitems))
exit(func)
