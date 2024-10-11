# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
v = resource_variable_ops.ResourceVariable(1.0)
self.evaluate(v.initializer)
result = array_ops.identity(v)
self.assertIsInstance(result, ops.Tensor)
self.assertAllEqual(result, v)
