# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_common_test.py
value = array_ops.constant(2.)
python_literal = 1.
replica_context = ds_context.get_replica_context()
fn_sets = {
    'assign': lambda var, value: var.assign(value),
    'assign_add': lambda var, value: var.assign_add(value),
    'assign_sub': lambda var, value: var.assign_sub(value),
}
replica_context._update(
    distributed_variable1, fn_sets[update_fn], args=(value,))
replica_context._update(
    distributed_variable1, fn_sets[update_fn], args=(python_literal,))
