# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_operators_test.py
x = ragged_factory_ops.constant([[1.0, -2.0], [8.0]])
y = ragged_factory_ops.constant([[4.0, 4.0], [2.0]])
self.assertAllEqual(abs(x), [[1.0, 2.0], [8.0]])

# pylint: disable=invalid-unary-operand-type
self.assertAllEqual((-x), [[-1.0, 2.0], [-8.0]])

self.assertAllEqual((x + y), [[5.0, 2.0], [10.0]])
self.assertAllEqual((3.0 + y), [[7.0, 7.0], [5.0]])
self.assertAllEqual((x + 3.0), [[4.0, 1.0], [11.0]])

self.assertAllEqual((x - y), [[-3.0, -6.0], [6.0]])
self.assertAllEqual((3.0 - y), [[-1.0, -1.0], [1.0]])
self.assertAllEqual((x + 3.0), [[4.0, 1.0], [11.0]])

self.assertAllEqual((x * y), [[4.0, -8.0], [16.0]])
self.assertAllEqual((3.0 * y), [[12.0, 12.0], [6.0]])
self.assertAllEqual((x * 3.0), [[3.0, -6.0], [24.0]])

self.assertAllEqual((x / y), [[0.25, -0.5], [4.0]])
self.assertAllEqual((y / x), [[4.0, -2.0], [0.25]])
self.assertAllEqual((2.0 / y), [[0.5, 0.5], [1.0]])
self.assertAllEqual((x / 2.0), [[0.5, -1.0], [4.0]])

self.assertAllEqual((x // y), [[0.0, -1.0], [4.0]])
self.assertAllEqual((y // x), [[4.0, -2.0], [0.0]])
self.assertAllEqual((2.0 // y), [[0.0, 0.0], [1.0]])
self.assertAllEqual((x // 2.0), [[0.0, -1.0], [4.0]])

self.assertAllEqual((x % y), [[1.0, 2.0], [0.0]])
self.assertAllEqual((y % x), [[0.0, -0.0], [2.0]])
self.assertAllEqual((2.0 % y), [[2.0, 2.0], [0.0]])
self.assertAllEqual((x % 2.0), [[1.0, 0.0], [0.0]])
