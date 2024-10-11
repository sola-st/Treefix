# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
"""Tests _get_dense_tensor() for input with shape=[2]."""
price = fc._numeric_column('price', shape=[2])
bucketized_price = fc._bucketized_column(price, boundaries=[0, 2, 4, 6])
with ops.Graph().as_default():
    builder = _LazyBuilder({'price': [[-1., 1.], [5., 6.]]})
    with _initialized_session():
        bucketized_price_tensor = bucketized_price._get_dense_tensor(builder)
        self.assertAllClose(
            # One-hot tensor.
            [[[1., 0., 0., 0., 0.], [0., 1., 0., 0., 0.]],
             [[0., 0., 0., 1., 0.], [0., 0., 0., 0., 1.]]],
            self.evaluate(bucketized_price_tensor))
