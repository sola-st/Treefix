# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_graph_reconstruction_test.py
with session.Session() as sess:
    u = variables.Variable([12.0], name="u")
    v = variables.Variable([30.0], name="v")
    w = math_ops.add(u, v, name="w")
    self.evaluate(u.initializer)
    self.evaluate(v.initializer)

    self._compareOriginalAndReconstructedGraphDefs(
        sess, w, expected_output=[42.0])
