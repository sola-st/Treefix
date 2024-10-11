# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
hashed_sparse = fc.categorical_column_with_hash_bucket('wire', 10)
transformation_cache = fc.FeatureTransformationCache({
    'wire':
        sparse_tensor.SparseTensor(
            values=['omar', 'stringer', 'marlo'],
            indices=[[0, 0], [1, 0], [1, 1]],
            dense_shape=[2, 2])
})
id_weight_pair = hashed_sparse.get_sparse_tensors(transformation_cache,
                                                  None)
self.assertIsNone(id_weight_pair.weight_tensor)
self.assertEqual(
    transformation_cache.get(hashed_sparse, None), id_weight_pair.id_tensor)
