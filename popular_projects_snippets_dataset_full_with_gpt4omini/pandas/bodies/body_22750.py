# Extracted from ./data/repos/pandas/pandas/core/series.py
# Validate axis argument
self._get_axis_number(axis)
result = SeriesApply(
    self, func=func, convert_dtype=True, args=args, kwargs=kwargs
).transform()
exit(result)
