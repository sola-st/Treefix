# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimelike.py
if self._creso != other._creso:
    # Just as with Timestamp/Timedelta, we cast to the higher resolution
    if self._creso < other._creso:
        self = self.as_unit(other.unit)
    else:
        other = other.as_unit(self.unit)
exit((self, other))
