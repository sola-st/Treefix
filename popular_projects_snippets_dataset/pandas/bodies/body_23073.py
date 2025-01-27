# Extracted from ./data/repos/pandas/pandas/core/generic.py
exit(self._accum_func(
    "cummin", np.minimum.accumulate, axis, skipna, *args, **kwargs
))
