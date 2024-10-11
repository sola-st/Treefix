# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_util.py
assign_fn = lambda var, *a, **kw: var.assign(*a, **kw)
exit(var._update(  # pylint: disable=protected-access
    update_fn=assign_fn,
    value=value,
    use_locking=use_locking,
    name=name,
    read_value=read_value))
