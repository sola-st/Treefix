# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
v = variables.Variable(
    1.0,
    trainable=False,
    synchronization=variables.VariableSynchronization.NONE,
    aggregation=variables.VariableAggregation.ONLY_FIRST_REPLICA,
)
self.assertEqual(variables.VariableSynchronization.NONE, v.synchronization)
self.assertEqual(
    variables.VariableAggregation.ONLY_FIRST_REPLICA, v.aggregation
)
root = autotrackable.AutoTrackable()
root.v = v
root = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)
self.assertEqual(False, root.v.trainable)
self.assertEqual(
    variables.VariableSynchronization.NONE, root.v.synchronization
)
self.assertEqual(
    variables.VariableAggregation.ONLY_FIRST_REPLICA, root.v.aggregation
)
