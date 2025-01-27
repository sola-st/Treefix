# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g_0 = ops.Graph()
g_1 = ops.Graph()
with g_0.as_default():
    x = constant_op.constant(1)
with g_1.as_default():
    y = constant_op.constant(2)
    with self.assertRaisesRegex(ValueError, "must be from the same graph"):
        y * x  # pylint: disable=pointless-statement
