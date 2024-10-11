# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
price = fc._numeric_column('price', shape=2)
with ops.Graph().as_default():
    features = {'price': [[1., 2.], [5., 6.]]}
    predictions = get_keras_linear_model_predictions(features, [price])
    price_var = get_linear_model_column_var(price)
    with _initialized_session() as sess:
        self.assertAllClose([[0.], [0.]], self.evaluate(price_var))
        sess.run(price_var.assign([[10.], [100.]]))
        self.assertAllClose([[210.], [650.]], self.evaluate(predictions))
