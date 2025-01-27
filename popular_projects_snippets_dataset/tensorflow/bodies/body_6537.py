# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_variable_test.py

def model_fn():
    v0 = variable_scope.variable(1.0, name="var0", aggregation=None)
    with variable_scope.variable_scope("common"):
        v1 = variable_scope.variable(1.0, name="var1")
        # This will pause the current thread, and execute the other thread.
        ds_context.get_replica_context().merge_call(lambda _: _)
        v2 = variable_scope.variable(
            1.0,
            name="var2",
            synchronization=variable_scope.VariableSynchronization.ON_READ,
            aggregation=variable_scope.VariableAggregation.SUM)
        v3 = variable_scope.variable(
            1.0,
            name="var3",
            synchronization=variable_scope.VariableSynchronization.ON_WRITE,
            aggregation=variable_scope.VariableAggregation.MEAN)

    exit((v0, v1, v2, v3))

with distribution.scope():
    v = variable_scope.variable(1.0, name="var-main0")
    self.assertEqual("var-main0:0", v.name)

    result = distribution.extended.call_for_each_replica(model_fn)
    self.assertEqual(4, len(result))
    v0, v1, v2, v3 = result
    self.assertTrue(distribute_utils.is_mirrored(v0))
    self.assertEqual("var0:0", v0.name)
    self.assertTrue(distribute_utils.is_mirrored(v1))
    self.assertEqual("common/var1:0", v1.name)
    self.assertTrue(distribute_utils.is_sync_on_read(v2))
    self.assertEqual("common/var2:0", v2.name)
    self.assertEqual(variable_scope.VariableAggregation.SUM, v2.aggregation)
    self.assertTrue(distribute_utils.is_mirrored(v3))
    self.assertEqual("common/var3:0", v3.name)
    self.assertEqual(variable_scope.VariableAggregation.MEAN, v3.aggregation)
