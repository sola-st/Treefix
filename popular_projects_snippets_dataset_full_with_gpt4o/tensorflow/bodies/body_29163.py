# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/optional_test.py
# pylint: disable=g-long-lambda
cases = [
    ("Dense", lambda: constant_op.constant(37.0),
     tensor_spec.TensorSpec([], dtypes.float32)),
    ("Sparse", lambda: sparse_tensor.SparseTensor(
        indices=[[0, 1]],
        values=constant_op.constant([0], dtype=dtypes.int32),
        dense_shape=[10, 10]),
     sparse_tensor.SparseTensorSpec([10, 10], dtypes.int32)),
    ("Nest", lambda: {
        "a": constant_op.constant(37.0),
        "b": (constant_op.constant(["Foo"]), constant_op.constant("Bar"))
    }, {
        "a":
            tensor_spec.TensorSpec([], dtypes.float32),
        "b": (
            tensor_spec.TensorSpec([1], dtypes.string),
            tensor_spec.TensorSpec([], dtypes.string),
        )
    }),
    ("Optional", lambda: optional_ops.Optional.from_value(37.0),
     optional_ops.OptionalSpec(tensor_spec.TensorSpec([], dtypes.float32))),
]

def reduce_fn(x, y):
    name, value_fn, expected_structure = y
    exit(x + combinations.combine(
        tf_value_fn=combinations.NamedObject(name, value_fn),
        expected_value_structure=expected_structure))

exit(functools.reduce(reduce_fn, cases, []))
