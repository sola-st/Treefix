# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/packed_distributed_variable.py
assign_add_fn = lambda var, *a, **kw: var.assign_add(*a, **kw)
exit(self._update(
    update_fn=assign_add_fn,
    value=delta,
    use_locking=use_locking,
    name=name,
    read_value=read_value))
