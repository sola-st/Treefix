# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
with g.as_default():
    w = constant_op.constant(0)
    x = constant_op.constant("")
    y = constant_op.constant(1)
    z = y + w
    z.op._update_input(0, x)  # pylint: disable=protected-access
with session.Session(graph=g) as sess:
    with self.assertRaisesRegex(
        errors.InvalidArgumentError,
        "Input 0 of node add was passed string from Const_1:0 incompatible "
        "with expected int32"):
        self.evaluate(z)
