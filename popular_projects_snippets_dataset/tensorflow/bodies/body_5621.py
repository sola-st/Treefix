# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2_test.py
g = ops.Graph()
with g.as_default():
    v = self.create_variable(1.)
    g.finalize()
    self.evaluate(v.initializer)
    # _as_graph_element shouldn't create new operations.
    self.assertEqual(self.evaluate(v._as_graph_element()), 1.)
