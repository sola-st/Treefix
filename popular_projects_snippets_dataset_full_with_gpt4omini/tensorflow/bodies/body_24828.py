# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_graph_reconstruction_test.py
with session.Session() as sess:
    a = variables.Variable(10.0, name="a")
    with ops.control_dependencies([a]):
        b = math_ops.add(a, a, name="b")
    with ops.control_dependencies([a, b]):
        c = math_ops.multiply(b, b, name="c")
    self.evaluate(a.initializer)

    self._compareOriginalAndReconstructedGraphDefs(
        sess, c, expected_output=400.0)
