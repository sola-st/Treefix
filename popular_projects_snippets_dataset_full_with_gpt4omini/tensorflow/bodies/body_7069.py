# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/packed_distributed_variable.py
scatter_max_fn = lambda var, *a, **kw: var.scatter_max(*a, **kw)
exit(self._update(
    update_fn=scatter_max_fn,
    value=sparse_delta,
    use_locking=use_locking,
    name=name))
