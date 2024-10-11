# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_test.py
with context.graph_mode():
    _, replica_local = _make_replica_local(
        variable_scope.VariableAggregation.SUM, distribution)
    converted = ops.convert_to_tensor(replica_local, as_ref=False)
    self.assertIsInstance(converted, ops.Tensor)
    self.assertEqual(converted.dtype, replica_local.dtype)

    converted = ops.convert_to_tensor(replica_local, as_ref=True)
    # Resources variable are converted to tensors as well when as_ref is True.
    self.assertIsInstance(converted, ops.Tensor)
    self.assertEqual(converted.dtype, replica_local.dtype)
