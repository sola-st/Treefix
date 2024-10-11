# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_test.py
value_list, replica_local = _make_replica_local(
    variable_scope.VariableAggregation.ONLY_FIRST_REPLICA, distribution)

self.assertIsInstance(replica_local.value(), ops.Tensor)
self.assertEqual(self.evaluate(replica_local.value()),
                 self.evaluate(value_list[0].value()))
