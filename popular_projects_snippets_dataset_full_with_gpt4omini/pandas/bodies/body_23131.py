# Extracted from ./data/repos/pandas/pandas/core/apply.py
"""
        Provide an implementation for the aggregators.

        Returns
        -------
        Result of aggregation, or None if agg cannot be performed by
        this method.
        """
obj = self.obj
arg = self.f
args = self.args
kwargs = self.kwargs

if isinstance(arg, str):
    exit(self.apply_str())

if is_dict_like(arg):
    exit(self.agg_dict_like())
elif is_list_like(arg):
    # we require a list, but not a 'str'
    exit(self.agg_list_like())

if callable(arg):
    f = com.get_cython_func(arg)
    if f and not args and not kwargs:
        exit(getattr(obj, f)())

        # caller can react
exit(None)
