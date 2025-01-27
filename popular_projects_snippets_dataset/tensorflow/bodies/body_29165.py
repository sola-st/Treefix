# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/optional_test.py
# pylint: disable=g-long-lambda
cases = [
    ("Dense", np.array([1, 2, 3], dtype=np.int32),
     lambda: constant_op.constant([4, 5, 6], dtype=dtypes.int32), True),
    ("Sparse",
     sparse_tensor.SparseTensorValue(
         indices=[[0, 0], [1, 1]],
         values=np.array([-1., 1.], dtype=np.float32),
         dense_shape=[2, 2]),
     lambda: sparse_tensor.SparseTensor(
         indices=[[0, 1], [1, 0]], values=[37.0, 42.0], dense_shape=[2, 2]),
     False),
    ("Nest", {
        "a":
            np.array([1, 2, 3], dtype=np.int32),
        "b":
            sparse_tensor.SparseTensorValue(
                indices=[[0, 0], [1, 1]],
                values=np.array([-1., 1.], dtype=np.float32),
                dense_shape=[2, 2])
    }, lambda: {
        "a":
            constant_op.constant([4, 5, 6], dtype=dtypes.int32),
        "b":
            sparse_tensor.SparseTensor(
                indices=[[0, 1], [1, 0]],
                values=[37.0, 42.0],
                dense_shape=[2, 2])
    }, False),
]

def reduce_fn(x, y):
    name, value, value_fn, gpu_compatible = y
    exit(x + combinations.combine(
        np_value=value,
        tf_value_fn=combinations.NamedObject(name, value_fn),
        gpu_compatible=gpu_compatible))

exit(functools.reduce(reduce_fn, cases, []))
