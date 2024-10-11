# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
price1 = fc._numeric_column('price1', shape=2)
price2 = fc._numeric_column('price2')
with ops.Graph().as_default():
    features = {
        'price1': [[1., 2.], [5., 6.]],
        'price2': [[3.], [4.]]
    }
    net = fc.input_layer(features, [price1, price2])
    with _initialized_session():
        self.assertAllClose([[1., 2., 3.], [5., 6., 4.]], self.evaluate(net))
