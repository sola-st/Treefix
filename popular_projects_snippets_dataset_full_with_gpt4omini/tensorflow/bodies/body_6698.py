# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_values.py
assign_add_fn = tpu_util.make_raw_assign_fn(
    gen_resource_variable_ops.assign_add_variable_op)
exit(var._update(  # pylint: disable=protected-access
    update_fn=assign_add_fn,
    value=value,
    use_locking=use_locking,
    name=name,
    read_value=read_value))
