# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
v = resource_variable_ops.ResourceVariable(1.)
self.evaluate(v.initializer)
v2 = resource_variable_ops.ResourceVariable(
    trainable=True, shape=(), dtype=dtypes.float32, handle=v.handle)
self.assertIs(v2.handle, v.handle)
self.assertAllEqual(ops.convert_to_tensor(v2), 1.)
