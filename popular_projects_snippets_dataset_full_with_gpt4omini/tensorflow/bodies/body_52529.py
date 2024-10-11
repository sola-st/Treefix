# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
price = fc.numeric_column('price', shape=[1, 2])
with ops.Graph().as_default():
    features = {'price': [[[1., 2.]], [[5., 6.]]]}
    predictions = fc_old.linear_model(features, [price])
    bias = get_linear_model_bias()
    price_var = get_linear_model_column_var(price)
    with _initialized_session() as sess:
        self.assertAllClose([0.], self.evaluate(bias))
        self.assertAllClose([[0.], [0.]], self.evaluate(price_var))
        self.assertAllClose([[0.], [0.]], self.evaluate(predictions))
        sess.run(price_var.assign([[10.], [100.]]))
        self.assertAllClose([[210.], [650.]], self.evaluate(predictions))
