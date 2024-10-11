# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_operators_test.py
# pylint: disable=invalid-unary-operand-type
a = ragged_factory_ops.constant([[True, True], [False]])
b = ragged_factory_ops.constant([[True, False], [False]])
self.assertAllEqual((~a), [[False, False], [True]])

self.assertAllEqual((a & b), [[True, False], [False]])
self.assertAllEqual((a & True), [[True, True], [False]])
self.assertAllEqual((True & b), [[True, False], [False]])

self.assertAllEqual((a | b), [[True, True], [False]])
self.assertAllEqual((a | False), [[True, True], [False]])
self.assertAllEqual((False | b), [[True, False], [False]])

self.assertAllEqual((a ^ b), [[False, True], [False]])
self.assertAllEqual((a ^ True), [[False, False], [True]])
self.assertAllEqual((True ^ b), [[False, True], [True]])
