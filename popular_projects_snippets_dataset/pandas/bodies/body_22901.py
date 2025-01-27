# Extracted from ./data/repos/pandas/pandas/core/generic.py
exit(all(
    self._get_axis(a).equals(other._get_axis(a)) for a in self._AXIS_ORDERS
))
