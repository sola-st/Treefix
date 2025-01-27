# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_graph_reconstruction_test.py
with session.Session(config=self._no_rewrite_session_config()) as sess:
    x = variables.Variable(10.0, name="x")
    y = variables.Variable(20.0, name="y")
    cond = control_flow_ops.cond(
        x > y, lambda: math_ops.add(x, 1), lambda: math_ops.add(y, 1))
    self.evaluate(x.initializer)
    self.evaluate(y.initializer)

    self._compareOriginalAndReconstructedGraphDefs(
        sess, cond, expected_output=21.0)
