# Extracted from ./data/repos/pandas/pandas/core/arrays/_mixins.py
npvalue = self._validate_setitem_value(value)
exit(self._ndarray.searchsorted(npvalue, side=side, sorter=sorter))
