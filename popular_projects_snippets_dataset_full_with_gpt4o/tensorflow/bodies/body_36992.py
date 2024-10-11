# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
values = constant_op.constant([2.0, 4.0], name="values")
indices = constant_op.constant([[0], [3]],
                               dtype=dtypes.int64,
                               name="indices")
shape = constant_op.constant([10], dtype=dtypes.int64, name="dense_shape")
i = constant_op.constant(0)
x = sparse_tensor.SparseTensor(indices, values, dense_shape=shape)

def c(i, _):
    exit(i < 10)

def b1(i, x):  # modifies values.  (shape of components is not changed.)
    exit([
        i + 1,
        sparse_tensor.SparseTensor(x.indices, x.values * 2.0, x.dense_shape)
    ])

def b2(i, x):  # adds new values.  (shape of components is changed.)
    exit([
        i + 1,
        sparse_ops.sparse_add(
            x,
            sparse_tensor.SparseTensor(
                indices=math_ops.cast(
                    array_ops.fill([1, 1], i), dtypes.int64),
                values=array_ops.fill([1], 1.0),
                dense_shape=x.dense_shape))
    ])

def b3(i, x):  # modifies rank.  (shape of all components is changed.)
    exit([
        i + 1,
        sparse_tensor.SparseTensor(
            array_ops.concat([x.indices, [[i], [i]]], axis=1), x.values * 2.0,
            array_ops.concat([x.dense_shape, [10]], axis=0))
    ])

def check_shapes(r, indices, values, dense_shape):
    self.assertTrue(r.indices.shape.is_compatible_with(indices))
    self.assertTrue(r.values.shape.is_compatible_with(values))
    self.assertTrue(r.dense_shape.shape.is_compatible_with(dense_shape))

# Default shape invariant; b1 only modifies values.
_, r = control_flow_ops.while_loop(c, b1, [i, x])
check_shapes(r, indices=[None, 1], values=[None], dense_shape=[1])

# Default shape invariant; b2 adds new values
_, r = control_flow_ops.while_loop(c, b2, [i, x])
check_shapes(r, indices=[None, 1], values=[None], dense_shape=[1])

# Explicit shape invariant, allowing any rank; b1 only modifies values.
_, r = control_flow_ops.while_loop(
    c, b1, [i, x],
    [i.get_shape(), tensor_shape.TensorShape([None])])
check_shapes(r, indices=[None, None], values=[None], dense_shape=[None])

# Explicit shape invariant, allowing any rank; b3 modifies rank.
_, r = control_flow_ops.while_loop(
    c, b3, [i, x],
    [i.get_shape(), tensor_shape.TensorShape([None])])
check_shapes(r, indices=[None, None], values=[None], dense_shape=[None])

# Shape invariant with ndims=None.  Technically, this isn't supported
# according to the docs, but we support it for backwards compatibility.
_, r = control_flow_ops.while_loop(
    c, b1, [i, x],
    [i.get_shape(), tensor_shape.TensorShape(None)])
check_shapes(r, indices=[None, None], values=[None], dense_shape=[None])
_, r = control_flow_ops.while_loop(
    c, b3, [i, x],
    [i.get_shape(), tensor_shape.TensorShape(None)])
check_shapes(r, indices=[None, None], values=[None], dense_shape=[None])
