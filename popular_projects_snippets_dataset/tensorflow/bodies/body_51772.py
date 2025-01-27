# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
# empty 1-D sparse tensor:
builder = _LazyBuilder(features={'a': sparse_tensor.SparseTensor(
    indices=np.reshape(np.array([], dtype=np.int64), (0, 1)),
    dense_shape=[0],
    values=np.array([]))})
with self.cached_session():
    spv = builder.get('a')
    self.assertAllEqual(np.array([0, 1], dtype=np.int64), spv.dense_shape)
    self.assertAllEqual(
        np.reshape(np.array([], dtype=np.int64), (0, 2)), spv.indices)
