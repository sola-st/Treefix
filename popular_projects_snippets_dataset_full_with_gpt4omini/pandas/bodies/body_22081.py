# Extracted from ./data/repos/pandas/pandas/core/groupby/generic.py
if isinstance(func, str):
    fast_path = lambda group: getattr(group, func)(*args, **kwargs)
    slow_path = lambda group: group.apply(
        lambda x: getattr(x, func)(*args, **kwargs), axis=self.axis
    )
else:
    fast_path = lambda group: func(group, *args, **kwargs)
    slow_path = lambda group: group.apply(
        lambda x: func(x, *args, **kwargs), axis=self.axis
    )
exit((fast_path, slow_path))
