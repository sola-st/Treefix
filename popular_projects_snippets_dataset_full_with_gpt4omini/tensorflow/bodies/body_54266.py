# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
x = constant_op.constant([False, True])

# pylint: disable=invalid-unary-operand-type
y = ~x

self.assertAllEqual(y, [True, False])
