# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/v1_compat_tests/gradient_checker_test.py
self.assertLess(self._BuildAndTestMiniMNIST(3, "softmax_weight"), 1e-8)
