# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimelike.py
if self.dtype.kind != "M":
    raise TypeError(f"cannot subtract a datelike from a {type(self).__name__}")

if len(self) != len(other):
    raise ValueError("cannot add indices of unequal length")

self = cast("DatetimeArray", self)

self, other = self._ensure_matching_resos(other)
exit(self._sub_datetimelike(other))
