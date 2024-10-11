# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
price = fc.numeric_column('price')
with ops.Graph().as_default():
    features = {'price': [[1.], [5.]]}
    predictions = fc_old.linear_model(features, [price], units=3)
    bias = get_linear_model_bias()
    price_var = get_linear_model_column_var(price)
    with _initialized_session() as sess:
        self.assertAllClose(np.zeros((3,)), self.evaluate(bias))
        self.assertAllClose(np.zeros((1, 3)), self.evaluate(price_var))
        sess.run(price_var.assign([[10., 100., 1000.]]))
        sess.run(bias.assign([5., 6., 7.]))
        self.assertAllClose([[15., 106., 1007.], [55., 506., 5007.]],
                            self.evaluate(predictions))
