# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
exit([
    i + 1,
    sparse_tensor.SparseTensor(
        array_ops.concat([x.indices, [[i], [i]]], axis=1), x.values * 2.0,
        array_ops.concat([x.dense_shape, [10]], axis=0))
])
