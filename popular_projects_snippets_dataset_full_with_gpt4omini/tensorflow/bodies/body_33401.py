# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_util_test.py
arr = rng.rand(2, 3, 4)
tensor, = linear_operator_util.broadcast_matrix_batch_dims([arr])
self.assertTrue(isinstance(tensor, ops.Tensor))

self.assertAllClose(arr, self.evaluate(tensor))
