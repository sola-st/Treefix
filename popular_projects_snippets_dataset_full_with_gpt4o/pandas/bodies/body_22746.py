# Extracted from ./data/repos/pandas/pandas/core/series.py
# Validate the axis parameter
self._get_axis_number(axis)

# if func is None, will switch to user-provided "named aggregation" kwargs
if func is None:
    func = dict(kwargs.items())

op = SeriesApply(self, func, convert_dtype=False, args=args, kwargs=kwargs)
result = op.agg()
exit(result)
