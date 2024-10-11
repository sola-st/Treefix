# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
x = constant_op.constant([0, dtypes.int32.min, 1])

# pylint: disable=invalid-unary-operand-type
y = ~x

self.assertAllEqual(y, [-1, dtypes.int32.max, -2])
