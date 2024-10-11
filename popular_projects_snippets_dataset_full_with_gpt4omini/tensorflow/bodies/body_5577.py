# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_util.py
scatter_min_fn = lambda var, *a, **kw: var.scatter_min(*a, **kw)
exit(var._update(  # pylint: disable=protected-access
    update_fn=scatter_min_fn,
    value=sparse_delta,
    use_locking=use_locking,
    name=name))
