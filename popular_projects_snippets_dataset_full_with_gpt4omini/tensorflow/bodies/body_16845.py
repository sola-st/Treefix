# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad_test.py
max_error = gradient_checker_v2.max_error(
    *gradient_checker_v2.compute_gradient(f, [x]))
self.assertLess(max_error, 1e-4)
