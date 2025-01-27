# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
a = fc.numeric_column('a', dtype=dtypes.int32, shape=(2,))
b = fc.bucketized_column(a, boundaries=(0, 1))
crossed1 = fc.crossed_column(['d1', 'd2'], 10)
crossed2 = fc.crossed_column([b, 'c', crossed1], 15, hash_key=5)
with ops.Graph().as_default():
    transformation_cache = fc.FeatureTransformationCache({
        'a':
            constant_op.constant(((-1., .5), (.5, 1.))),
        'c':
            sparse_tensor.SparseTensor(
                indices=((0, 0), (1, 0), (1, 1)),
                values=['cA', 'cB', 'cC'],
                dense_shape=(2, 2)),
        'd1':
            sparse_tensor.SparseTensor(
                indices=((0, 0), (1, 0), (1, 1)),
                values=['d1A', 'd1B', 'd1C'],
                dense_shape=(2, 2)),
        'd2':
            sparse_tensor.SparseTensor(
                indices=((0, 0), (1, 0), (1, 1)),
                values=['d2A', 'd2B', 'd2C'],
                dense_shape=(2, 2)),
    })
    id_weight_pair = crossed2.get_sparse_tensors(transformation_cache, None)

    self.evaluate(variables_lib.global_variables_initializer())
    self.evaluate(lookup_ops.tables_initializer())

    id_tensor_eval = self.evaluate(id_weight_pair.id_tensor)
    self.assertAllEqual(
        ((0, 0), (0, 1), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
         (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (1, 12), (1, 13),
         (1, 14), (1, 15)), id_tensor_eval.indices)
    # Check exact hashed output. If hashing changes this test will break.
    # All values are within [0, hash_bucket_size).
    expected_values = (6, 14, 0, 13, 8, 8, 10, 12, 2, 0, 1, 9, 8, 12, 2, 0,
                       10, 11)
    self.assertAllEqual(expected_values, id_tensor_eval.values)
    self.assertAllEqual((2, 16), id_tensor_eval.dense_shape)
