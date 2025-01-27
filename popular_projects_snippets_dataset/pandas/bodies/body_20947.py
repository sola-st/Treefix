# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimes.py
if dtype is None and self.tz:
    # The default for tz-aware is object, to preserve tz info
    dtype = object

exit(super().__array__(dtype=dtype))
