# Extracted from ./data/repos/pandas/pandas/core/frame.py
# NB: we can't just use self.loc[key] = value because that
#  operates on labels and we need to operate positional for
#  backwards-compat, xref GH#31469
self._check_setitem_copy()
self.iloc[key] = value
