# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/packed_distributed_variable.py
scatter_mul_fn = lambda var, *a, **kw: var.scatter_mul(*a, **kw)
exit(self._update(
    update_fn=scatter_mul_fn,
    value=sparse_delta,
    use_locking=use_locking,
    name=name))
