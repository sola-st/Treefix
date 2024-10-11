# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_util.py
scatter_sub_fn = lambda var, *a, **kw: var.scatter_sub(*a, **kw)
exit(var._update(  # pylint: disable=protected-access
    update_fn=scatter_sub_fn,
    value=sparse_delta,
    use_locking=use_locking,
    name=name))
