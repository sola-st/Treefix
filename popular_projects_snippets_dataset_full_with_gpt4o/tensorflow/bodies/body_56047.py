# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_def_to_graph_test.py
fdef = self._build_function_def()
g = function_def_to_graph.function_def_to_graph(fdef)
self.assertEqual(g.name, "_whats_in_a_name")
with self.session(graph=g) as sess:
    inputs = sess.run(g.inputs, feed_dict={"x:0": 2, "y:0": 3})
    self.assertSequenceEqual(inputs, [2.0, 3.0])
    outputs = sess.run(g.outputs, feed_dict={"x:0": 2, "y:0": 3})
    self.assertSequenceEqual(outputs, [13.0, 35.0])
