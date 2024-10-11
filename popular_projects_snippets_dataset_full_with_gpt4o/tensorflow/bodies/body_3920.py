# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/capture_container_test.py
container = self._prepare_function_captures()
a = constant_op.constant(1)
b = constant_op.constant(2.0)
c = constant_op.constant([1, 2, 3])
spec_a = tensor_spec.TensorSpec([], np.int32)
spec_b = tensor_spec.TensorSpec([], np.float32)
spec_c = tensor_spec.TensorSpec([3,], np.int32)

value = [{"a": a}, [b, c]]
lam = lambda: value
graph = func_graph.FuncGraph("graph")
with graph.as_default():
    placeholder = container._create_capture_placeholder(lam)
self.assertLen(placeholder, 2)
self.assertIn("a", placeholder[0])
self.assertLen(placeholder[1], 2)

placeholder_a = placeholder[0]["a"]
placeholder_b = placeholder[1][0]
placeholder_c = placeholder[1][1]
self.assertEqual(placeholder_a.shape, spec_a.shape)
self.assertEqual(placeholder_a.dtype, spec_a.dtype)
self.assertEqual(placeholder_b.shape, spec_b.shape)
self.assertEqual(placeholder_b.dtype, spec_b.dtype)
self.assertEqual(placeholder_c.shape, spec_c.shape)
self.assertEqual(placeholder_c.dtype, spec_c.dtype)
