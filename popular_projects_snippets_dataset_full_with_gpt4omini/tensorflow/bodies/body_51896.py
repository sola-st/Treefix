# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
price1 = fc._numeric_column('price1', shape=2)
price2 = fc._numeric_column('price2')
with ops.Graph().as_default():
    features = {
        'price1': [[1., 2.], [5., 6.]],
        'price2': [[3.], [4.]]
    }
    predictions = fc.linear_model(features, [price1, price2])
    bias = get_linear_model_bias()
    price1_var = get_linear_model_column_var(price1)
    price2_var = get_linear_model_column_var(price2)
    with _initialized_session() as sess:
        self.assertAllClose([0.], self.evaluate(bias))
        self.assertAllClose([[0.], [0.]], self.evaluate(price1_var))
        self.assertAllClose([[0.]], self.evaluate(price2_var))
        self.assertAllClose([[0.], [0.]], self.evaluate(predictions))
        sess.run(price1_var.assign([[10.], [100.]]))
        sess.run(price2_var.assign([[1000.]]))
        sess.run(bias.assign([7.]))
        self.assertAllClose([[3217.], [4657.]], self.evaluate(predictions))
