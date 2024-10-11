# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
price = fc._numeric_column('price', shape=[1, 2])
with ops.Graph().as_default():
    features = {'price': [[[1., 2.]], [[5., 6.]]]}
    net = fc.input_layer(features, [price])
    with _initialized_session():
        self.assertAllClose([[1., 2.], [5., 6.]], self.evaluate(net))
