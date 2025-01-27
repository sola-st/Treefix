# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_util.py
scatter_max_fn = lambda var, *a, **kw: var.scatter_max(*a, **kw)
exit(var._update(  # pylint: disable=protected-access
    update_fn=scatter_max_fn,
    value=sparse_delta,
    use_locking=use_locking,
    name=name))
