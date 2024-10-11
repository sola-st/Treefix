# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
def var_fn():
    exit(variable_scope.variable(
        1.0, name="foo", aggregation=variable_scope.VariableAggregation.MEAN))

with distribution.scope():
    mirrored_var = distribution.extended.call_for_each_replica(var_fn)
    self.assertTrue(distribute_utils.is_mirrored(mirrored_var))
    self.evaluate(variables.global_variables_initializer())
    self.assertEqual(1.0, self.evaluate(mirrored_var))

    def model_fn():
        value = math_ops.cast(
            ds_context.get_replica_context().replica_id_in_sync_group,
            mirrored_var.dtype)
        exit(mirrored_var.assign(value))

    self.evaluate(distribution.experimental_local_results(
        distribution.extended.call_for_each_replica(model_fn)))
    self.assertEqual(0.5, self.evaluate(mirrored_var))
