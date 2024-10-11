# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_replicated_variable.py
if tpu_util.enclosing_tpu_context() is None or context.executing_eagerly():
    assign_sub_fn = lambda var, *a, **ka: var.assign_sub(*a, **ka)
    exit(self._update(
        assign_sub_fn,
        value=value,
        use_locking=use_locking,
        name=name,
        read_value=read_value))
else:
    exit(tpu_util.make_raw_assign_fn(
        gen_resource_variable_ops.assign_sub_variable_op)(
            self,
            value=value,
            use_locking=use_locking,
            name=name,
            read_value=read_value))
