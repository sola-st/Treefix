# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_variable_test.py
if isinstance(distribution.extended, tpu_strategy.TPUExtended):
    if context.executing_eagerly():
        self.skipTest("TPU doesn't support pure eager")
    else:
        self.skipTest("b/152076846")

with distribution.scope():
    v = variables_lib.Variable(
        0., synchronization=synchronization, aggregation=aggregation)

def assert_is_tensor_like(v):
    # We can't use Python literals because they are treated as non-distributed
    # values is not allowed when aggregation is SUM. See
    # `cross_device_ops.reduce_non_distributed_value`.
    delta = array_ops.identity(1.)
    self.assertIsInstance(v.assign(delta), core.Tensor)
    self.assertIsInstance(v.assign_sub(delta), core.Tensor)
    self.assertIsInstance(v.assign_add(delta), core.Tensor)

# In cross replica context we return a PerReplica which is not Tensor like
# all the time yet.
if (synchronization == variables_lib.VariableSynchronization.ON_READ and
    aggregation != variables_lib.VariableAggregation.SUM):
    assert_is_tensor_like(v)

# In replica context.
distribution.run(assert_is_tensor_like, args=(v,))
