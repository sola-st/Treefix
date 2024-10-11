# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/packed_distributed_variable.py
scatter_div_fn = lambda var, *a, **kw: var.scatter_div(*a, **kw)
exit(self._update(
    update_fn=scatter_div_fn,
    value=sparse_delta,
    use_locking=use_locking,
    name=name))
