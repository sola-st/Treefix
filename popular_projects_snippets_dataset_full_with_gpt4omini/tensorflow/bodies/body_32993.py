# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_algebra_test.py
for (k, v) in _MATMUL.items():
    self.assertEqual(v, _registered_matmul(k[0], k[1]))
