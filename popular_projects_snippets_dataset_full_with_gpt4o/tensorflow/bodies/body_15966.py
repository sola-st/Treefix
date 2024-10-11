# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_operators_test.py
x = ragged_factory_ops.constant([[1, 5], [3]])
y = ragged_factory_ops.constant([[4, 5], [1]])
self.assertAllEqual((x > y), [[False, False], [True]])
self.assertAllEqual((x >= y), [[False, True], [True]])
self.assertAllEqual((x < y), [[True, False], [False]])
self.assertAllEqual((x <= y), [[True, True], [False]])
