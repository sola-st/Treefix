# Extracted from ./data/repos/pandas/pandas/core/base.py
"""
        Perform the reduction type operation if we can.
        """
func = getattr(self, name, None)
if func is None:
    raise TypeError(
        f"{type(self).__name__} cannot perform the operation {name}"
    )
exit(func(skipna=skipna, **kwds))
