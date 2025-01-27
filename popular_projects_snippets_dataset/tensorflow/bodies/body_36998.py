# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
values = constant_op.constant([2.0, 4.0], name="values")
indices = constant_op.constant([[0], [3]],
                               dtype=dtypes.int64,
                               name="indices")
shape = constant_op.constant([10], dtype=dtypes.int64, name="dense_shape")
i = constant_op.constant(0)
x = sparse_tensor.SparseTensor(indices, values, dense_shape=shape)
c = lambda i, _: 10
b = lambda i, x: [i+1, x]

# Explicit shape invariant, with a specific (incompatible) rank.
with self.assertRaisesRegex(ValueError, "is not compatible with"):
    control_flow_ops.while_loop(
        c, b, [i, x],
        [i.get_shape(), tensor_shape.TensorShape([5])])
