# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_util.py
scatter_update_fn = lambda var, *a, **kw: var.scatter_update(*a, **kw)
exit(var._update(  # pylint: disable=protected-access
    update_fn=scatter_update_fn,
    value=sparse_delta,
    use_locking=use_locking,
    name=name))
