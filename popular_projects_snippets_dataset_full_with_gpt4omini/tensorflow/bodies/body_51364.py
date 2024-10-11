# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2_test.py
path = self._no_signatures_model()
root = load.load(path)
fn = root.prune("x:0", "out:0")
self.assertEqual(2., self.evaluate(fn(x=array_ops.ones([]))))
root.graph.as_graph_element("x:0")
