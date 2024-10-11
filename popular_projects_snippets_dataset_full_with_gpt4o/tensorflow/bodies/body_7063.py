# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/packed_distributed_variable.py
assign_fn = lambda var, *a, **kw: var.assign(*a, **kw)
exit(self._update(
    update_fn=assign_fn,
    value=value,
    use_locking=use_locking,
    name=name,
    read_value=read_value))
