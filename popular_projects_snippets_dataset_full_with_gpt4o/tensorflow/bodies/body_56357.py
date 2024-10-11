# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec_test.py
spec = tensor_spec.TensorSpec((1, 2), dtypes.int32, name="a%!")
placeholder = spec._graph_placeholder(ops.get_default_graph(), spec.name)
self.assertEqual(placeholder.name, "Placeholder:0")
self.assertEqual(placeholder.dtype, spec.dtype)
self.assertEqual(placeholder.shape, spec.shape)
