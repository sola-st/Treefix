# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
i = constant_op.constant(0)
x = ragged_factory_ops.constant([[1, 2], [3], [4, 5, 6]])
c = lambda i, _: i < 10

def b1(i, x):  # Adds new values to rows (but doesn't create new rows)
    exit([
        i + 1,
        array_ops.concat([x, x], axis=1)
    ])

def b2(i, x):  # Adds new rows.
    exit([
        i + 1,
        array_ops.concat([x, x], axis=0)
    ])

def check_shapes(r, values, splits):
    self.assertTrue(r.values.shape.is_compatible_with(values))
    self.assertTrue(r.row_splits.shape.is_compatible_with(splits))

# Default shape invariant; b1 adds new values to rows.
_, r = control_flow_ops.while_loop(c, b1, [i, x])
check_shapes(r, values=[None], splits=[4])

# Default shape invariant; b2 adds new rows (not allowed).
if not context.executing_eagerly():
    with self.assertRaises(ValueError):
        _, r = control_flow_ops.while_loop(c, b2, [i, x])

    # Explicit shape invariant; b1 adds new values to rows.
    # (deprecated: use TensorShape instead of RaggedTensorSpec)
_, r = control_flow_ops.while_loop(
    c, b1, [i, x],
    [i.get_shape(), tensor_shape.TensorShape([None, None])])
check_shapes(r, values=[None], splits=[None])

# Explicit shape invariant; b1 adds new values to rows.
_, r = control_flow_ops.while_loop(
    c, b1, [i, x],
    [i.get_shape(), ragged_tensor.RaggedTensorSpec([None, None],
                                                   dtypes.int32)])
check_shapes(r, values=[None], splits=[None])

# Explicit shape invariant; b2 adds new rows.
_, r = control_flow_ops.while_loop(
    c, b2, [i, x],
    [i.get_shape(), ragged_tensor.RaggedTensorSpec([None, None],
                                                   dtypes.int32)])
check_shapes(r, values=[None], splits=[None])
