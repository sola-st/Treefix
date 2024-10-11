# Extracted from ./data/repos/pandas/pandas/core/arrays/interval.py
breaks = _maybe_convert_platform_interval(breaks)

exit(cls.from_arrays(breaks[:-1], breaks[1:], closed, copy=copy, dtype=dtype))
