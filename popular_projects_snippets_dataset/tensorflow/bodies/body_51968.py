# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with ops.Graph().as_default():
    features = features = {'a': [0.]}
    net = fc.input_layer(features, fc._numeric_column('a'))
    with _initialized_session():
        self.assertAllClose([[0.]], self.evaluate(net))
