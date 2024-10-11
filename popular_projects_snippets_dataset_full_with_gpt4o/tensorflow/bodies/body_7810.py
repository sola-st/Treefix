# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_common_test.py
if strategy_test_lib.is_tpu_strategy(strategy) and (not tf_function):
    self.skipTest('Skip TPUStrategy + eager combination.')
with strategy.scope():
    distributed_variable1 = variables.Variable(5.0)

def replica_fn():
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

if tf_function:
    replica_fn = def_function.function(replica_fn)
strategy.run(replica_fn)

expected_result = {'assign': 1., 'assign_add': 8., 'assign_sub': 2.}
self.assertAllEqual(
    strategy.experimental_local_results(distributed_variable1),
    [expected_result[update_fn]] * _get_num_replicas_per_client(strategy))
