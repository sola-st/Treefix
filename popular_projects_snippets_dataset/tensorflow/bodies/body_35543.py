# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_grad_test.py
ret = random_grad.add_leading_unit_dimensions(1.0, 2)
self.assertAllEqual(ret.shape, [1, 1])
