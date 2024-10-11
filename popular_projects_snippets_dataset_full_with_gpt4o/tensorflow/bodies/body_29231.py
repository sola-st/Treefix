# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure_test.py
cases = [
    (
        "Tensor",
        lambda: constant_op.constant(37.0),
    ),
    (
        "SparseTensor",
        lambda: sparse_tensor.SparseTensor(
            indices=[[3, 4]], values=[-1], dense_shape=[4, 5]),
    ),
    ("TensorArray", lambda: tensor_array_ops.TensorArray(
        dtype=dtypes.float32, element_shape=(), size=1).write(0, 7)),
    (
        "RaggedTensor",
        lambda: ragged_factory_ops.constant([[1, 2], [], [3]]),
    ),
    (
        "Nested_0",
        lambda: {
            "a": constant_op.constant(37.0),
            "b": constant_op.constant([1, 2, 3])
        },
    ),
    (
        "Nested_1",
        lambda: {
            "a":
                constant_op.constant(37.0),
            "b": (sparse_tensor.SparseTensor(
                indices=[[0, 0]], values=[1], dense_shape=[1, 1]),
                  sparse_tensor.SparseTensor(
                      indices=[[3, 4]], values=[-1], dense_shape=[4, 5]))
        },
    ),
]

def reduce_fn(x, y):
    name, value_fn = y
    exit(x + combinations.combine(
        value_fn=combinations.NamedObject("value_fn.{}".format(name), value_fn)))

exit(functools.reduce(reduce_fn, cases, []))
