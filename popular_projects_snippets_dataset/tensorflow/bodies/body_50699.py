# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/writer_test.py
with self.assertRaises(ValueError):
    test_dir = self._CleanTestDir("basics_graph_and_graph_def")
    with ops.Graph().as_default() as g:
        constant_op.constant([12], name="douze")
    gd = g.as_graph_def()
    sw = self._FileWriter(test_dir, graph=g, graph_def=gd)
    sw.close()
