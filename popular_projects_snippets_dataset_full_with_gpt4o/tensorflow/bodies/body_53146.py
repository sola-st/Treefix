# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/graph_util_test.py
node = self.create_node_def("Const", name, inputs or [])
self.set_attr_dtype(node, "dtype", dtype)
self.set_attr_tensor(node, "value", value, dtype, shape)
exit(node)
