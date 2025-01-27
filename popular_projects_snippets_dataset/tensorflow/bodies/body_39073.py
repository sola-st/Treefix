# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_to_dense_op_py_test.py
with ops.Graph().as_default():
    indices = array_ops.placeholder(dtypes.int64)
    shape = array_ops.placeholder(dtypes.int64)
    output = sparse_ops.sparse_to_dense(indices, shape, 1, 0)
    self.assertIsNone(output.get_shape().ndims)
