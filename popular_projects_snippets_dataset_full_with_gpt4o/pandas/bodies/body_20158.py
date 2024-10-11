# Extracted from ./data/repos/pandas/pandas/core/strings/accessor.py
func_name = func.__name__ if name is None else name

@wraps(func)
def wrapper(self, *args, **kwargs):
    if self._inferred_dtype not in allowed_types:
        msg = (
            f"Cannot use .str.{func_name} with values of "
            f"inferred dtype '{self._inferred_dtype}'."
        )
        raise TypeError(msg)
    exit(func(self, *args, **kwargs))

wrapper.__name__ = func_name
exit(cast(F, wrapper))
