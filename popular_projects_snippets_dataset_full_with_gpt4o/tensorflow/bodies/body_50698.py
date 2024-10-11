# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/writer_test.py
test_dir = self._CleanTestDir("basics_positional_graph_def")
with ops.Graph().as_default() as g:
    constant_op.constant([12], name="douze")
gd = g.as_graph_def()
sw = self._FileWriter(test_dir, gd)
sw.close()
self.assertEventsWithGraph(test_dir, g, False)
