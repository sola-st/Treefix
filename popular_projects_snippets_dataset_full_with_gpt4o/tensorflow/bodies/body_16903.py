# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradient_checker_v2_test.py
self.assertLess(self._BuildAndTestMiniMNIST(2, "hidden_bias"), 1e-8)
