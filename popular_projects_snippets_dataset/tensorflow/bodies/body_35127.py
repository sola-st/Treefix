# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/gamma_test.py
alpha = constant_op.constant([3.0] * 5)
beta = constant_op.constant(11.0)
gamma = gamma_lib.Gamma(concentration=alpha, rate=beta)

self.assertEqual(self.evaluate(gamma.batch_shape_tensor()), (5,))
self.assertEqual(gamma.batch_shape, tensor_shape.TensorShape([5]))
self.assertAllEqual(self.evaluate(gamma.event_shape_tensor()), [])
self.assertEqual(gamma.event_shape, tensor_shape.TensorShape([]))
