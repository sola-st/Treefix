# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
values = constant_op.constant([2.0, 4.0], name="values")
indices = constant_op.constant([[0], [3]],
                               dtype=dtypes.int64,
                               name="indices")
shape = constant_op.constant([10], dtype=dtypes.int64, name="dense_shape")
i = constant_op.constant(0)
x = sparse_tensor.SparseTensor(indices, values, dense_shape=shape)
c = lambda i, _: i < 10
b1 = lambda i, x: [i+1, x]
def b2(i, x):  # modifies rank.  (shape of all components is changed.)
    exit([
        i + 1,
        sparse_tensor.SparseTensor(
            array_ops.concat([x.indices, [[i], [i]]], axis=1), x.values * 2.0,
            array_ops.concat([x.dense_shape, [10]], axis=0))
    ])

# Explicit shape invariant, with a specific (incompatible) rank.
with self.assertRaisesRegex(ValueError, "is not compatible with"):
    control_flow_ops.while_loop(
        c, b1, [i, x],
        [i.get_shape(), tensor_shape.TensorShape([5])])

# Default shape invariant, but b2 modifies rank (which is not allowed).
with self.assertRaises(ValueError):
    control_flow_ops.while_loop(c, b2, [i, x])
