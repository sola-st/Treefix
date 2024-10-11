# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
# Test that we don't reduce a non-per-replica value with the "sum"
# aggregation type.
def var_fn():
    v = variable_scope.variable(
        1.0, name="foo", aggregation=variable_scope.VariableAggregation.SUM)
    exit(v)

with distribution.scope():
    mirrored_var = distribution.extended.call_for_each_replica(var_fn)
    self.assertTrue(distribute_utils.is_mirrored(mirrored_var))
    self.evaluate(variables.global_variables_initializer())

    def model_fn():
        exit(mirrored_var.assign(5.0))

    if distribution.extended._use_merge_call():
        with self.assertRaisesRegex(
            ValueError, "A non-DistributedValues value 5.0 cannot be reduced "
            "with the given reduce op ReduceOp.SUM."):
            self.evaluate(distribution.experimental_local_results(
                distribution.extended.call_for_each_replica(model_fn)))
    else:
        result = self.evaluate(
            distribution.experimental_local_results(
                distribution.extended.call_for_each_replica(model_fn)))
        self.assertAllEqual(result[0], 5.0)
