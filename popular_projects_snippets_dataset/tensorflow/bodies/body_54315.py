# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
with g.as_default():
    w = constant_op.constant(2, shape=[3, 1])
    x = constant_op.constant(0, shape=[3, 1])
    y = constant_op.constant(1, shape=[2, 2])
    z = w + x
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    r"Cannot update edge, incompatible shapes: \[2,2\] and \[3,1\]"):
    z.op._update_input(0, y)  # pylint: disable=protected-access
