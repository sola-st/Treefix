# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
graph = ops.Graph()
with graph.as_default():
    z = constant_op.constant(0)
    x = constant_op.constant(1)
    y = constant_op.constant(2)
    y.op._add_control_input(z.op)  # pylint: disable=protected-access
    y.op._add_control_input(x.op)  # pylint: disable=protected-access
    x.op._add_control_input(y.op)  # pylint: disable=protected-access
with self.session(graph=graph) as sess:
    with self.assertRaisesRegex(
        errors.InvalidArgumentError,
        "Graph is invalid, contains a cycle with 2 nodes"):
        self.evaluate(x)
