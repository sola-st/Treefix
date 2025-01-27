# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/writer_test.py
test_dir = self._CleanTestDir("basics_named_graph")
with ops.Graph().as_default() as g:
    constant_op.constant([12], name="douze")
sw = self._FileWriter(test_dir, graph=g)
sw.close()
self.assertEventsWithGraph(test_dir, g, True)
