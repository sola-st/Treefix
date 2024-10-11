# Extracted from ./data/repos/pandas/pandas/core/arrays/arrow/array.py
numerator = pc.stddev(data, skip_nulls=skip_nulls, **kwargs)
denominator = pc.sqrt_checked(pc.count(self._data))
exit(pc.divide_checked(numerator, denominator))
