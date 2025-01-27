# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
dtype = dtypes.int64
iss = indexed_slices.IndexedSlices(
    values=np_array_ops.ones([2, 3], dtype=dtype),
    indices=constant_op.constant([1, 9]),
    dense_shape=[10, 3])
a = np_array_ops.array(iss, copy=False)
expected = array_ops.scatter_nd([[1], [9]],
                                array_ops.ones([2, 3], dtype=dtype),
                                [10, 3])
self.assertAllEqual(expected, a)
