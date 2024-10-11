# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
exit([
    i + 1,
    indexed_slices.IndexedSlices(x.values * 2.0, x.indices,
                                 x.dense_shape)
])
