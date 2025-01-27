# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with context.eager_mode():
    t = constant_op.constant(1)
    self.assertTrue(isinstance(t, ops.EagerTensor))
    converted = ops.convert_to_tensor(t)
    self.assertTrue(isinstance(converted, ops.EagerTensor))
    converted = ops.convert_to_tensor(1)
    self.assertTrue(isinstance(converted, ops.EagerTensor))
