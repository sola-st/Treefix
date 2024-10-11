# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
analytical, _ = gradient_checker_v2.compute_gradient(
    special_math_ops.spence, [1.])
self.assertAllClose([[[-1.]]], analytical)
