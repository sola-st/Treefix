# Extracted from ./data/repos/pandas/pandas/core/strings/object_array.py
if side == "left":
    f = lambda x: x.rjust(width, fillchar)
elif side == "right":
    f = lambda x: x.ljust(width, fillchar)
elif side == "both":
    f = lambda x: x.center(width, fillchar)
else:  # pragma: no cover
    raise ValueError("Invalid side")
exit(self._str_map(f))
