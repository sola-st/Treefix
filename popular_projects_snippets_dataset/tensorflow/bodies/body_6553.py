# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_variable_test.py

all_v_sum = {}
all_v_mean = {}
components_sum = {}
components_mean = {}

def model_fn():
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

with distribution.scope():
    # Create "sum" and "mean" versions of SyncOnReadVariables.
    ret_ops, ret_v_sum, ret_v_mean, regrouped_sum, regrouped_mean = (
        distribution.extended.call_for_each_replica(model_fn))
    # Should see the same wrapping instance in all replicas.
    self.assertIs(all_v_sum[0], ret_v_sum)
    self.assertIs(all_v_mean[0], ret_v_mean)
    self.assertIs(all_v_sum[0], all_v_sum[1])
    self.assertIs(all_v_mean[0], all_v_mean[1])

    # Regroup should recover the same wrapper.
    self.assertIs(ret_v_sum, regrouped_sum)
    self.assertIs(ret_v_mean, regrouped_mean)
    self.assertIsNot(components_sum[0], components_sum[1])
    self.assertIsNot(components_mean[0], components_mean[1])

    # Apply updates
    self.evaluate(variables.global_variables_initializer())
    self.evaluate([
        y for x in ret_ops  # pylint: disable=g-complex-comprehension
        for y in distribution.experimental_local_results(x)
    ])
    expected_sum = 0.0
    expected_mean = 0.0
    for i, _ in enumerate(distribution.extended.worker_devices):
        # Should see different values on different devices.
        v_sum_value = self.evaluate(
            distribution.experimental_local_results(ret_v_sum)[i].read_value())
        v_mean_value = self.evaluate(
            distribution.experimental_local_results(ret_v_mean)[i].read_value())
        expected = i + 3.0
        self.assertEqual(expected, v_sum_value)
        expected_sum += expected
        expected = i * 6.0
        self.assertEqual(expected, v_mean_value)
        expected_mean += expected
    expected_mean /= len(distribution.extended.worker_devices)

    # Without get(device), should return the value you get by
    # applying the reduction across all replicas (whether you use
    # read_var(), get(), or nothing).
    self.assertEqual(expected_sum, self.evaluate(
        distribution.extended.read_var(ret_v_sum)))
    self.assertEqual(expected_mean, self.evaluate(
        distribution.extended.read_var(ret_v_mean)))
    self.assertEqual(expected_sum, self.evaluate(ret_v_sum._get()))
    self.assertEqual(expected_mean, self.evaluate(ret_v_mean._get()))
    self.assertEqual(expected_sum, self.evaluate(ret_v_sum))
    self.assertEqual(expected_mean, self.evaluate(ret_v_mean))
