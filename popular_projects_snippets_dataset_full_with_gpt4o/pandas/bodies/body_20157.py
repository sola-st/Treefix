# Extracted from ./data/repos/pandas/pandas/core/strings/accessor.py
if self._inferred_dtype not in allowed_types:
    msg = (
        f"Cannot use .str.{func_name} with values of "
        f"inferred dtype '{self._inferred_dtype}'."
    )
    raise TypeError(msg)
exit(func(self, *args, **kwargs))
