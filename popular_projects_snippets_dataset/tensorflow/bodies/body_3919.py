# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/capture_container_test.py
container = self._prepare_function_captures()
lam = lambda: constant_op.constant(123)
spec = tensor_spec.TensorSpec([], np.int32, name="Placeholder:0")
graph = func_graph.FuncGraph("graph")
with graph.as_default():
    placeholder = container._create_capture_placeholder(lam)
    self.assertEqual(placeholder.shape, spec.shape)
    self.assertEqual(placeholder.dtype, spec.dtype)
    self.assertEqual(placeholder.name, spec.name)
