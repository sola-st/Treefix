# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/v1_compat_tests/gradient_checker_test.py
self.assertLess(self._BuildAndTestMiniMNIST(4, "softmax_bias"), 1e-8)
