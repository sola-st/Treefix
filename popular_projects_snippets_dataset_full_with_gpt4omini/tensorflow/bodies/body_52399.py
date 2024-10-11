# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
# empty 1-D sparse tensor:
transformation_cache = fc.FeatureTransformationCache(
    features={
        'a':
            sparse_tensor.SparseTensor(
                indices=np.reshape(np.array([], dtype=np.int64), (0, 1)),
                dense_shape=[0],
                values=np.array([]))
    })

spv = self.evaluate(transformation_cache.get('a', None))
self.assertAllEqual(np.array([0, 1], dtype=np.int64), spv.dense_shape)
self.assertAllEqual(
    np.reshape(np.array([], dtype=np.int64), (0, 2)), spv.indices)
