# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
price_a = fc._numeric_column('price_a')
price_b = fc._numeric_column('price_b')
with ops.Graph().as_default():
    features = {
        'price_a': [[1.]],
        'price_b': [[3.]],
    }
    net1 = fc.input_layer(features, [price_a, price_b])
    net2 = fc.input_layer(features, [price_b, price_a])
    with _initialized_session():
        self.assertAllClose([[1., 3.]], self.evaluate(net1))
        self.assertAllClose([[1., 3.]], self.evaluate(net2))
