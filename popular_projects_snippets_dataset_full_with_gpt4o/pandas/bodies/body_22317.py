# Extracted from ./data/repos/pandas/pandas/core/resample.py
x = self._shallow_copy(x, groupby=self.groupby)

if isinstance(f, str):
    exit(getattr(x, f)(**kwargs))

exit(x.apply(f, *args, **kwargs))
