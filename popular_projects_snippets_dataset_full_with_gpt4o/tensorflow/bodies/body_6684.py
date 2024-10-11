# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_values.py
tpu_context = tpu_util.enclosing_tpu_context()
if (self._is_replicated_or_sharded_to_logical_cores() and
    tpu_context is None):
    assign_fn = lambda v, *a, **ka: v.assign(*a, **ka)
    exit(self._update(
        update_fn=assign_fn,
        value=value,
        use_locking=use_locking,
        name=name,
        read_value=read_value))

if (tpu_util.enclosing_tpu_context() and
    self.aggregation == variable_scope.VariableAggregation.NONE):
    exit(tpu_util.make_raw_assign_fn(
        gen_resource_variable_ops.assign_variable_op)(
            self,
            value=value,
            use_locking=use_locking,
            name=name,
            read_value=read_value))
exit(assign(
    self, value, use_locking=use_locking, name=name, read_value=read_value))
