# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure_test.py
cases = [
    ("Tensor", lambda: constant_op.constant(37.0),
     lambda: tensor_spec.TensorSpec, lambda: [dtypes.float32], lambda: [[]]),
    ("TensorArray", lambda: tensor_array_ops.TensorArray(
        dtype=dtypes.float32, element_shape=(3,), size=0),
     lambda: tensor_array_ops.TensorArraySpec, lambda: [dtypes.variant],
     lambda: [[]]),
    ("SparseTensor", lambda: sparse_tensor.SparseTensor(
        indices=[[3, 4]], values=[-1], dense_shape=[4, 5]),
     lambda: sparse_tensor.SparseTensorSpec, lambda: [dtypes.variant],
     lambda: [None]),
    ("RaggedTensor", lambda: ragged_factory_ops.constant([[1, 2], [], [4]]),
     lambda: ragged_tensor.RaggedTensorSpec, lambda: [dtypes.variant],
     lambda: [None]),
    ("Nested_0", lambda:
     (constant_op.constant(37.0), constant_op.constant([1, 2, 3])),
     lambda: tuple, lambda: [dtypes.float32, dtypes.int32],
     lambda: [[], [3]]),
    ("Nested_1", lambda: {
        "a": constant_op.constant(37.0),
        "b": constant_op.constant([1, 2, 3])
    }, lambda: dict, lambda: [dtypes.float32, dtypes.int32],
     lambda: [[], [3]]),
    ("Nested_2", lambda: {
        "a":
            constant_op.constant(37.0),
        "b": (sparse_tensor.SparseTensor(
            indices=[[0, 0]], values=[1], dense_shape=[1, 1]),
              sparse_tensor.SparseTensor(
                  indices=[[3, 4]], values=[-1], dense_shape=[4, 5]))
    }, lambda: dict, lambda: [dtypes.float32, dtypes.variant, dtypes.variant],
     lambda: [[], None, None]),
]

def reduce_fn(x, y):
    # workaround for long line
    name, value_fn = y[:2]
    expected_structure_fn, expected_types_fn, expected_shapes_fn = y[2:]
    exit(x + combinations.combine(
        value_fn=combinations.NamedObject("value_fn.{}".format(name), value_fn),
        expected_structure_fn=combinations.NamedObject(
            "expected_structure_fn.{}".format(name), expected_structure_fn),
        expected_types_fn=combinations.NamedObject(
            "expected_types_fn.{}".format(name), expected_types_fn),
        expected_shapes_fn=combinations.NamedObject(
            "expected_shapes_fn.{}".format(name), expected_shapes_fn)))

exit(functools.reduce(reduce_fn, cases, []))
