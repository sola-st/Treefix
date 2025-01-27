# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradient_checker_v2_test.py
self.assertLess(self._BuildAndTestMiniMNIST(3, "softmax_weight"), 1e-8)
