# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
"""Tests _LinearModel for input with shape=[1]."""
price = fc._numeric_column('price', shape=[1])
bucketized_price = fc._bucketized_column(price, boundaries=[0, 2, 4, 6])
with ops.Graph().as_default():
    features = {'price': [[-1.], [1.], [5.], [6.]]}
    predictions = get_keras_linear_model_predictions(features,
                                                     [bucketized_price])
    bias = get_linear_model_bias()
    bucketized_price_var = get_linear_model_column_var(bucketized_price)
    with _initialized_session() as sess:
        self.assertAllClose([0.], self.evaluate(bias))
        # One weight variable per bucket, all initialized to zero.
        self.assertAllClose([[0.], [0.], [0.], [0.], [0.]],
                            self.evaluate(bucketized_price_var))
        self.assertAllClose([[0.], [0.], [0.], [0.]],
                            self.evaluate(predictions))
        sess.run(
            bucketized_price_var.assign([[10.], [20.], [30.], [40.], [50.]]))
        # price -1. is in the 0th bucket, whose weight is 10.
        # price 1. is in the 1st bucket, whose weight is 20.
        # price 5. is in the 3rd bucket, whose weight is 40.
        # price 6. is in the 4th bucket, whose weight is 50.
        self.assertAllClose([[10.], [20.], [40.], [50.]],
                            self.evaluate(predictions))
        sess.run(bias.assign([1.]))
        self.assertAllClose([[11.], [21.], [41.], [51.]],
                            self.evaluate(predictions))
