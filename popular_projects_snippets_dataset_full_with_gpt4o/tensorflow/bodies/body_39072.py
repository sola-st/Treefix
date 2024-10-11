# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_to_dense_op_py_test.py
with ops.Graph().as_default():
    indices = array_ops.placeholder(dtypes.int64)

    shape = [4, 5, 6]
    output = sparse_ops.sparse_to_dense(indices, shape, 1, 0)
    self.assertEqual(output.get_shape(), [4, 5, 6])

    shape = array_ops.placeholder(dtypes.int64, shape=(3,))
    output = sparse_ops.sparse_to_dense(indices, shape, 1, 0)
    self.assertEqual(output.get_shape().as_list(), [None, None, None])
