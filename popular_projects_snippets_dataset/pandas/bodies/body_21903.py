# Extracted from ./data/repos/pandas/pandas/core/window/rolling.py
result = ResamplerWindowApply(self, func, args=args, kwargs=kwargs).agg()
if result is None:

    # these must apply directly
    result = func(self)

exit(result)
