# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
c = lambda i, _: i < 10
b = lambda i, x: (i + 1, x)
i = constant_op.constant(0)
x = sparse_tensor.SparseTensor([[0]], [1.0], [10])
shape_invariants = [
    tensor_spec.TensorSpec([], dtype=dtypes.int32),
    sparse_tensor.SparseTensorSpec([None])]
control_flow_ops.while_loop(c, b, [i, x], shape_invariants)

x2 = constant_op.constant([1])
with self.assertRaises(TypeError):
    control_flow_ops.while_loop(c, b, [i, x2], shape_invariants)

x3 = ragged_factory_ops.constant([[1, 2], [3]])
with self.assertRaises(TypeError):
    control_flow_ops.while_loop(c, b, [i, x3], shape_invariants)

i2 = constant_op.constant(0.0)
with self.assertRaises(TypeError):
    control_flow_ops.while_loop(c, b, [i2, x], shape_invariants)
