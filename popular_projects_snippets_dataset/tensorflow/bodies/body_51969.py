# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with ops.Graph().as_default():
    features = features = {'a': [0.], 'b': [1.]}
    columns = (fc._numeric_column(key) for key in features)
    net = fc.input_layer(features, columns)
    with _initialized_session():
        self.assertAllClose([[0., 1.]], self.evaluate(net))
