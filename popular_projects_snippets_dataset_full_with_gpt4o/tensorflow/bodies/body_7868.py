# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/ps_values.py
assign_sub_fn = lambda var, *a, **kw: var.assign_sub(*a, **kw)
exit(self._assign_func(f=assign_sub_fn, *args, **kwargs))
