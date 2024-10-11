# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
test_dir = self._get_test_dir("write_graph_dir")
variables.VariableV1(
    [[1, 2, 3], [4, 5, 6]], dtype=dtypes.float32, name="v0")
path = graph_io.write_graph(ops_lib.get_default_graph(),
                            os.path.join(test_dir, "l1"), "graph.pbtxt")
truth = os.path.join(test_dir, "l1", "graph.pbtxt")
self.assertEqual(path, truth)
self.assertTrue(os.path.exists(path))
