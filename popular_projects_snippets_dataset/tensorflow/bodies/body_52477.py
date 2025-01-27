# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
"""Same as test_get_sparse_tensors, but with simpler values."""
a = fc.numeric_column('a', dtype=dtypes.int32, shape=(2,))
b = fc.bucketized_column(a, boundaries=(0, 1))
crossed = fc.crossed_column([b, 'c'], hash_bucket_size=5, hash_key=5)
with ops.Graph().as_default():
    transformation_cache = fc.FeatureTransformationCache({
        'a':
            constant_op.constant(((-1., .5), (.5, 1.))),
        'c':
            sparse_tensor.SparseTensor(
                indices=((0, 0), (1, 0), (1, 1)),
                values=['cA', 'cB', 'cC'],
                dense_shape=(2, 2)),
    })
    id_weight_pair = crossed.get_sparse_tensors(transformation_cache, None)

    self.evaluate(variables_lib.global_variables_initializer())
    self.evaluate(lookup_ops.tables_initializer())

    id_tensor_eval = self.evaluate(id_weight_pair.id_tensor)
    self.assertAllEqual(((0, 0), (0, 1), (1, 0), (1, 1), (1, 2), (1, 3)),
                        id_tensor_eval.indices)
    # Check exact hashed output. If hashing changes this test will break.
    # All values are within [0, hash_bucket_size).
    expected_values = (1, 0, 1, 3, 4, 2)
    self.assertAllEqual(expected_values, id_tensor_eval.values)
    self.assertAllEqual((2, 4), id_tensor_eval.dense_shape)
