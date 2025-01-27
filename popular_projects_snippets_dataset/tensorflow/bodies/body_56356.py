# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec_test.py
spec = tensor_spec.TensorSpec((2, 3), dtypes.float32, name="test")
placeholder = spec._graph_placeholder(ops.get_default_graph(), spec.name)
self.assertEqual(placeholder.name, f"{spec.name}:0")
self.assertEqual(placeholder.dtype, spec.dtype)
self.assertEqual(placeholder.shape, spec.shape)
