# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_values.py
if (tpu_util.enclosing_tpu_context() and
    var.aggregation == variable_scope.VariableAggregation.NONE):
    exit(tpu_util.make_raw_assign_fn(
        gen_resource_variable_ops.assign_variable_op)(
            var,
            value=value,
            use_locking=use_locking,
            name=name,
            read_value=read_value))
exit(assign(
    var, value, use_locking=use_locking, name=name, read_value=read_value))
