# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
out = op_def_library.apply_op("Simple", a=3)
self.assertEqual(out.graph, ops.get_default_graph())
