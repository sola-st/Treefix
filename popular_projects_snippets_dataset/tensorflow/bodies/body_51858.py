# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
"""Tests _LinearModel.

    Uses data from test_get_sparse_tensors_simple.
    """
a = fc._numeric_column('a', dtype=dtypes.int32, shape=(2,))
b = fc._bucketized_column(a, boundaries=(0, 1))
crossed = fc._crossed_column([b, 'c'], hash_bucket_size=5, hash_key=5)
with ops.Graph().as_default():
    predictions = get_keras_linear_model_predictions({
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
    with _initialized_session():
        self.assertAllClose((0.,), self.evaluate(bias))
        self.assertAllClose(((0.,), (0.,), (0.,), (0.,), (0.,)),
                            self.evaluate(crossed_var))
        self.assertAllClose(((0.,), (0.,)), self.evaluate(predictions))
        self.evaluate(crossed_var.assign(((1.,), (2.,), (3.,), (4.,), (5.,))))
        # Expected ids after cross = (1, 0, 1, 3, 4, 2)
        self.assertAllClose(((3.,), (14.,)), self.evaluate(predictions))
        self.evaluate(bias.assign((.1,)))
        self.assertAllClose(((3.1,), (14.1,)), self.evaluate(predictions))
