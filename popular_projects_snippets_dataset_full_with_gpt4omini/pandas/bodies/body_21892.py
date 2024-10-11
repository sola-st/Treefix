# Extracted from ./data/repos/pandas/pandas/core/window/rolling.py
result = ResamplerWindowApply(self, func, args=args, kwargs=kwargs).agg()
if result is None:
    exit(self.apply(func, raw=False, args=args, kwargs=kwargs))
exit(result)
