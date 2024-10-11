# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
with g.as_default():
    x = constant_op.constant(1)
with self.assertRaisesRegex(
    errors.OutOfRangeError,
    r"Cannot update edge. Input index \[1\] is greater than the number of "
    r"total inputs \[0\]."):
    x.op._update_input(1, x)  # pylint: disable=protected-access
