# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
exit([
    i + 1,
    sparse_tensor.SparseTensor(x.indices, x.values * 2.0, x.dense_shape)
])
