# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
"""Tests linear_model() for input with shape=[2]."""
price = fc._numeric_column('price', shape=[2])
bucketized_price = fc._bucketized_column(price, boundaries=[0, 2, 4, 6])
with ops.Graph().as_default():
    features = {'price': [[-1., 1.], [5., 6.]]}
    predictions = fc.linear_model(features, [bucketized_price])
    bias = get_linear_model_bias()
    bucketized_price_var = get_linear_model_column_var(bucketized_price)
    with _initialized_session() as sess:
        self.assertAllClose([0.], self.evaluate(bias))
        # One weight per bucket per input column, all initialized to zero.
        self.assertAllClose(
            [[0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.]],
            self.evaluate(bucketized_price_var))
        self.assertAllClose([[0.], [0.]], self.evaluate(predictions))
        sess.run(bucketized_price_var.assign(
            [[10.], [20.], [30.], [40.], [50.],
             [60.], [70.], [80.], [90.], [100.]]))
        # 1st example:
        #   price -1. is in the 0th bucket, whose weight is 10.
        #   price 1. is in the 6th bucket, whose weight is 70.
        # 2nd example:
        #   price 5. is in the 3rd bucket, whose weight is 40.
        #   price 6. is in the 9th bucket, whose weight is 100.
        self.assertAllClose([[80.], [140.]], self.evaluate(predictions))
        sess.run(bias.assign([1.]))
        self.assertAllClose([[81.], [141.]], self.evaluate(predictions))
