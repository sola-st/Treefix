# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_variable_test.py
if isinstance(distribution.extended,
              tpu_strategy.TPUExtended) and context.executing_eagerly():
    self.skipTest("TPU doesn't support pure eager")

with distribution.scope():
    v = variables_lib.Variable(
        0., synchronization=synchronization, aggregation=aggregation)
# In cross replica context.
self.assertIsInstance(v, core.Tensor)
# In replica context.
distribution.run(lambda v: self.assertIsInstance(v, core.Tensor), args=(v,))
