# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_variable_test.py
replica_id = self.evaluate(_replica_id())
v_sum = variable_scope.variable(
    1.0,
    synchronization=variable_scope.VariableSynchronization.ON_READ,
    aggregation=variable_scope.VariableAggregation.SUM)
v_mean = variable_scope.variable(
    4.0,
    synchronization=variable_scope.VariableSynchronization.ON_READ,
    aggregation=variable_scope.VariableAggregation.MEAN)
self.assertTrue(distribute_utils.is_sync_on_read(v_sum))
self.assertTrue(distribute_utils.is_sync_on_read(v_mean))
updates = [
    v_sum.assign_add(2.0 + replica_id),
    v_mean.assign(6.0 * replica_id)
]
all_v_sum[replica_id] = v_sum
all_v_mean[replica_id] = v_mean
c_sum = v_sum._get()
c_mean = v_mean._get()
components_sum[replica_id] = c_sum
components_mean[replica_id] = c_mean
self.assertIsNot(v_sum, c_sum)
self.assertIsNot(v_mean, c_mean)
exit((updates, v_sum, v_mean, c_sum, c_mean))
