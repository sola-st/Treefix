# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
"""Tests linear_model.

    Uses data from test_get_sparse_tensors_simple.
    """
a = fc_old._numeric_column('a', dtype=dtypes.int32, shape=(2,))
b = fc.bucketized_column(a, boundaries=(0, 1))
crossed = fc.crossed_column([b, 'c'], hash_bucket_size=5, hash_key=5)
with ops.Graph().as_default():
    predictions = fc_old.linear_model({
        'a':
            constant_op.constant(((-1., .5), (.5, 1.))),
        'c':
            sparse_tensor.SparseTensor(
                indices=((0, 0), (1, 0), (1, 1)),
                values=['cA', 'cB', 'cC'],
                dense_shape=(2, 2)),
    }, (crossed,))
    bias = get_linear_model_bias()
    crossed_var = get_linear_model_column_var(crossed)
    with _initialized_session() as sess:
        self.assertAllClose((0.,), self.evaluate(bias))
        self.assertAllClose(((0.,), (0.,), (0.,), (0.,), (0.,)),
                            self.evaluate(crossed_var))
        self.assertAllClose(((0.,), (0.,)), self.evaluate(predictions))
        sess.run(crossed_var.assign(((1.,), (2.,), (3.,), (4.,), (5.,))))
        # Expected ids after cross = (1, 0, 1, 3, 4, 2)
        self.assertAllClose(((3.,), (14.,)), self.evaluate(predictions))
        sess.run(bias.assign((.1,)))
        self.assertAllClose(((3.1,), (14.1,)), self.evaluate(predictions))
