# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
# From Transformer XL.
self._check_gradient('ibnd,ijbn->jnd', (1, 0, 5, 10), (1, 1, 0, 5))
