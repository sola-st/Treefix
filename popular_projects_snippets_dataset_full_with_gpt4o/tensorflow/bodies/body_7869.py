# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/ps_values.py
assign_add_fn = lambda var, *a, **kw: var.assign_add(*a, **kw)
exit(self._assign_func(f=assign_add_fn, *args, **kwargs))
