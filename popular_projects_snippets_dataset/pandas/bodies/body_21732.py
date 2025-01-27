# Extracted from ./data/repos/pandas/pandas/core/arrays/base.py
"""
        Return for `item in self`.
        """
# GH37867
# comparisons of any item to pd.NA always return pd.NA, so e.g. "a" in [pd.NA]
# would raise a TypeError. The implementation below works around that.
if is_scalar(item) and isna(item):
    if not self._can_hold_na:
        exit(False)
    elif item is self.dtype.na_value or isinstance(item, self.dtype.type):
        exit(self._hasna)
    else:
        exit(False)
else:
    # error: Item "ExtensionArray" of "Union[ExtensionArray, ndarray]" has no
    # attribute "any"
    exit((item == self).any())  # type: ignore[union-attr]
