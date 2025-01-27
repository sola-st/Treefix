# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/ps_values.py
assign_fn = lambda var, *a, **kw: var.assign(*a, **kw)
exit(self._assign_func(f=assign_fn, *args, **kwargs))
