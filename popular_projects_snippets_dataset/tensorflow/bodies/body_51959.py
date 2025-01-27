# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
features = {'a': [0.]}
input_layer = InputLayer(fc._numeric_column('a'))
inputs = self.evaluate(input_layer(features))
self.assertAllClose([[0.]], inputs)
