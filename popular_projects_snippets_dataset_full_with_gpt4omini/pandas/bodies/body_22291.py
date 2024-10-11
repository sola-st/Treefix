# Extracted from ./data/repos/pandas/pandas/core/resample.py

result = ResamplerWindowApply(self, func, args=args, kwargs=kwargs).agg()
if result is None:
    how = func
    result = self._groupby_and_aggregate(how, *args, **kwargs)

exit(result)
