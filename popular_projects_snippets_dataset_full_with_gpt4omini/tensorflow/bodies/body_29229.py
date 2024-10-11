# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure_test.py
cases = [
    ("Tensor", lambda: constant_op.constant(37.0),
     lambda: constant_op.constant(42.0), lambda: constant_op.constant([5])),
    ("TensorArray", lambda: tensor_array_ops.TensorArray(
        dtype=dtypes.float32, element_shape=(3,), size=0),
     lambda: tensor_array_ops.TensorArray(
         dtype=dtypes.float32, element_shape=(3,), size=0),
     lambda: tensor_array_ops.TensorArray(
         dtype=dtypes.int32, element_shape=(), size=0)),
    ("SparseTensor", lambda: sparse_tensor.SparseTensor(
        indices=[[3, 4]], values=[-1], dense_shape=[4, 5]),
     lambda: sparse_tensor.SparseTensor(
         indices=[[1, 2]], values=[42], dense_shape=[4, 5]), lambda:
     sparse_tensor.SparseTensor(indices=[[3]], values=[-1], dense_shape=[5])),
    ("Nested", lambda: {
        "a": constant_op.constant(37.0),
        "b": constant_op.constant([1, 2, 3])
    }, lambda: {
        "a": constant_op.constant(42.0),
        "b": constant_op.constant([4, 5, 6])
    }, lambda: {
        "a": constant_op.constant([1, 2, 3]),
        "b": constant_op.constant(37.0)
    }),
]

def reduce_fn(x, y):
    name, value1_fn, value2_fn, value3_fn = y
    exit(x + combinations.combine(
        value1_fn=combinations.NamedObject("value1_fn.{}".format(name),
                                           value1_fn),
        value2_fn=combinations.NamedObject("value2_fn.{}".format(name),
                                           value2_fn),
        value3_fn=combinations.NamedObject("value3_fn.{}".format(name),
                                           value3_fn)))

exit(functools.reduce(reduce_fn, cases, []))
