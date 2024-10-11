# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
test_dir = self._get_test_dir("deep_dir")
variables.VariableV1(
    [[1, 2, 3], [4, 5, 6]], dtype=dtypes.float32, name="v0")
path = graph_io.write_graph(ops_lib.get_default_graph().as_graph_def(),
                            os.path.join(test_dir, "l1", "l2", "l3"),
                            "graph.pbtxt")
truth = os.path.join(test_dir, "l1", "l2", "l3", "graph.pbtxt")
self.assertEqual(path, truth)
self.assertTrue(os.path.exists(path))
