# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/uniform_test.py
a = constant_op.constant([-3.0] * 5)
b = constant_op.constant(11.0)
uniform = uniform_lib.Uniform(low=a, high=b)

self.assertEqual(self.evaluate(uniform.batch_shape_tensor()), (5,))
self.assertEqual(uniform.batch_shape, tensor_shape.TensorShape([5]))
self.assertAllEqual(self.evaluate(uniform.event_shape_tensor()), [])
self.assertEqual(uniform.event_shape, tensor_shape.TensorShape([]))
