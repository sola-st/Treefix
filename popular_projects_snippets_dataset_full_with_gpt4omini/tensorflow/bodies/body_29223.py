# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure_test.py
cases = [
    ("Tensor", lambda: constant_op.constant(37.0), lambda: [
        constant_op.constant(38.0),
        array_ops.placeholder(dtypes.float32), 42.0,
        np.array(42.0, dtype=np.float32)
    ], lambda: [constant_op.constant([1.0, 2.0]),
                constant_op.constant(37)]),
    # TODO(b/209081027): add Python constant and TF constant to the
    # incompatible branch after ResourceVariable becoming a CompositeTensor.
    ("Variable", lambda: variables.Variable(100.0),
     lambda: [variables.Variable(99.0)],
     lambda: [1]),
    ("TensorArray", lambda: tensor_array_ops.TensorArray(
        dtype=dtypes.float32, element_shape=(3,), size=0), lambda: [
            tensor_array_ops.TensorArray(
                dtype=dtypes.float32, element_shape=(3,), size=0),
            tensor_array_ops.TensorArray(
                dtype=dtypes.float32, element_shape=(3,), size=10)
        ], lambda: [
            tensor_array_ops.TensorArray(
                dtype=dtypes.int32, element_shape=(3,), size=0),
            tensor_array_ops.TensorArray(
                dtype=dtypes.float32, element_shape=(), size=0)
        ]),
    ("SparseTensor", lambda: sparse_tensor.SparseTensor(
        indices=[[3, 4]], values=[-1], dense_shape=[4, 5]),
     lambda: [
         sparse_tensor.SparseTensor(
             indices=[[1, 1], [3, 4]], values=[10, -1], dense_shape=[4, 5]),
         sparse_tensor.SparseTensorValue(
             indices=[[1, 1], [3, 4]], values=[10, -1], dense_shape=[4, 5]),
         array_ops.sparse_placeholder(dtype=dtypes.int32),
         array_ops.sparse_placeholder(dtype=dtypes.int32, shape=[None, None])
     ], lambda: [
         constant_op.constant(37, shape=[4, 5]),
         sparse_tensor.SparseTensor(
             indices=[[3, 4]], values=[-1], dense_shape=[5, 6]),
         array_ops.sparse_placeholder(
             dtype=dtypes.int32, shape=[None, None, None]),
         sparse_tensor.SparseTensor(
             indices=[[3, 4]], values=[-1.0], dense_shape=[4, 5])
     ]),
    ("RaggedTensor", lambda: ragged_factory_ops.constant([[1, 2], [], [3]]),
     lambda: [
         ragged_factory_ops.constant([[1, 2], [3, 4], []]),
         ragged_factory_ops.constant([[1], [2, 3, 4], [5]]),
     ], lambda: [
         ragged_factory_ops.constant(1),
         ragged_factory_ops.constant([1, 2]),
         ragged_factory_ops.constant([[1], [2]]),
         ragged_factory_ops.constant([["a", "b"]]),
     ]),
    ("Nested", lambda: {
        "a": constant_op.constant(37.0),
        "b": constant_op.constant([1, 2, 3])
    }, lambda: [{
        "a": constant_op.constant(15.0),
        "b": constant_op.constant([4, 5, 6])
    }], lambda: [{
        "a": constant_op.constant(15.0),
        "b": constant_op.constant([4, 5, 6, 7])
    }, {
        "a": constant_op.constant(15),
        "b": constant_op.constant([4, 5, 6])
    }, {
        "a":
            constant_op.constant(15),
        "b":
            sparse_tensor.SparseTensor(
                indices=[[0], [1], [2]], values=[4, 5, 6], dense_shape=[3])
    }, (constant_op.constant(15.0), constant_op.constant([4, 5, 6]))]),
]

def reduce_fn(x, y):
    name, original_value_fn, compatible_values_fn, incompatible_values_fn = y
    exit(x + combinations.combine(
        original_value_fn=combinations.NamedObject(
            "original_value_fn.{}".format(name), original_value_fn),
        compatible_values_fn=combinations.NamedObject(
            "compatible_values_fn.{}".format(name), compatible_values_fn),
        incompatible_values_fn=combinations.NamedObject(
            "incompatible_values_fn.{}".format(name), incompatible_values_fn)))

exit(functools.reduce(reduce_fn, cases, []))
