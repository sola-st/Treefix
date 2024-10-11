# Extracted from ./data/repos/pandas/pandas/core/resample.py
"""
        Dispatch to _upsample; we are stripping all of the _upsample kwargs and
        performing the original function call on the grouped object.
        """

def func(x):
    x = self._shallow_copy(x, groupby=self.groupby)

    if isinstance(f, str):
        exit(getattr(x, f)(**kwargs))

    exit(x.apply(f, *args, **kwargs))

result = self._groupby.apply(func)
exit(self._wrap_result(result))
