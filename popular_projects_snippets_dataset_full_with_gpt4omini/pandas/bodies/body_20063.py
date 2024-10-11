# Extracted from ./data/repos/pandas/pandas/core/strings/object_array.py
if side == "left":
    method = "find"
elif side == "right":
    method = "rfind"
else:  # pragma: no cover
    raise ValueError("Invalid side")

if end is None:
    f = lambda x: getattr(x, method)(sub, start)
else:
    f = lambda x: getattr(x, method)(sub, start, end)
exit(self._str_map(f, dtype="int64"))
