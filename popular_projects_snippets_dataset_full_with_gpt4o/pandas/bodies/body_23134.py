# Extracted from ./data/repos/pandas/pandas/core/apply.py
"""
        Compute transform in the case of a string or callable func
        """
obj = self.obj
args = self.args
kwargs = self.kwargs

if isinstance(func, str):
    exit(self._try_aggregate_string_function(obj, func, *args, **kwargs))

if not args and not kwargs:
    f = com.get_cython_func(func)
    if f:
        exit(getattr(obj, f)())

        # Two possible ways to use a UDF - apply or call directly
try:
    exit(obj.apply(func, args=args, **kwargs))
except Exception:
    exit(func(obj, *args, **kwargs))
