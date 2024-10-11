# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
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
