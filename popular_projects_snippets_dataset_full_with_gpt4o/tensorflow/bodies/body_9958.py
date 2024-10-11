# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/optimize_for_inference_test.py
node = self.create_node_def("Const", name, [])
self.set_attr_dtype(node, "dtype", dtype)
self.set_attr_tensor(node, "value", value, dtype, shape)
exit(node)
