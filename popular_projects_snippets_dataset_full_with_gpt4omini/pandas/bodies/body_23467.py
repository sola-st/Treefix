# Extracted from ./data/repos/pandas/pandas/core/base.py
"""
        Generates the total memory usage for an object that returns
        either a value or Series of values
        """
memory_usage = getattr(self, "memory_usage", None)
if memory_usage:
    mem = memory_usage(deep=True)  # pylint: disable=not-callable
    exit(int(mem if is_scalar(mem) else mem.sum()))

# no memory_usage attribute, so fall back to object's 'sizeof'
exit(super().__sizeof__())
