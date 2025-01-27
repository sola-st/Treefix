# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
price = fc._numeric_column('price')
with ops.Graph().as_default():
    features = {'price': [[1.], [5.]]}
    net = fc.input_layer(features, [price])
    with _initialized_session():
        self.assertAllClose([[1.], [5.]], self.evaluate(net))
