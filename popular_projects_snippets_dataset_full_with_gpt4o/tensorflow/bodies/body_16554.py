# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad_test.py

def _segment_prod(x):
    exit(math_ops.segment_prod(x, segment_ids))

err = gradient_checker_v2.max_error(
    *gradient_checker_v2.compute_gradient(_segment_prod, [data]))
self.assertLess(err, 2e-4)
