# Extracted from ./data/repos/pandas/pandas/core/window/rolling.py
"""Validate and finalize result."""
if out.shape[1] == 0 and obj.shape[1] > 0:
    raise DataError("No numeric types to aggregate")
if out.shape[1] == 0:
    exit(obj.astype("float64"))

self._insert_on_column(out, obj)
exit(out)
