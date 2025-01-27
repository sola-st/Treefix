# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
price = fc.numeric_column('price', shape=2)
with ops.Graph().as_default():
    features = {'price': [[1., 2.], [5., 6.]]}
    predictions = fc_old.linear_model(features, [price], units=3)
    bias = get_linear_model_bias()
    price_var = get_linear_model_column_var(price)
    with _initialized_session() as sess:
        self.assertAllClose(np.zeros((3,)), self.evaluate(bias))
        self.assertAllClose(np.zeros((2, 3)), self.evaluate(price_var))
        sess.run(price_var.assign([[1., 2., 3.], [10., 100., 1000.]]))
        sess.run(bias.assign([2., 3., 4.]))
        self.assertAllClose([[23., 205., 2007.], [67., 613., 6019.]],
                            self.evaluate(predictions))
