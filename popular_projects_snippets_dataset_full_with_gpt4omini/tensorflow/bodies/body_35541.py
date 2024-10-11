# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_grad_test.py
ret = random_grad.add_leading_unit_dimensions(array_ops.ones([3, 2, 1]), 3)
self.assertAllEqual(ret.shape, [1, 1, 1, 3, 2, 1])
