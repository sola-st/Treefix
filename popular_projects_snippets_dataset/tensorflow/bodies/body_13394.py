# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sparse_ops_test.py
x = np.asarray([1, 2])
y = np.asarray([[1, 0, 0], [0, 0, 2]])
for dtype in [dtypes.qint8, dtypes.qint16, dtypes.quint8, dtypes.quint16]:
    sp = sparse_tensor.SparseTensor(
        indices=[[0, 0], [1, 2]],
        values=x.astype(dtype.as_numpy_dtype),
        dense_shape=[2, 3])
    v = self.evaluate(sparse_ops.sparse_tensor_to_dense(sp))
    self.assertAllEqual(
        y.astype(dtype.as_numpy_dtype), v.astype(dtype.as_numpy_dtype))
