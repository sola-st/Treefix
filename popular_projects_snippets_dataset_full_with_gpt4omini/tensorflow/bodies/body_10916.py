# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with ops.Graph().as_default() as graph:
    init = constant_op.constant(100.0)
    var = variables.Variable(init)
    gradient = gradients.gradients(graph.as_graph_element(var), var)
    self.assertIsNotNone(gradient)
