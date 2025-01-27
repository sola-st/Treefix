# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
graph = ops.Graph()
with graph.as_default():
    out = op_def_library.apply_op("Simple", a=3)
    self.assertEqual(out.graph, graph)
