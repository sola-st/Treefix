# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
with ops.Graph().as_default():
    features = features = {'a': [0.]}
    net = fc_old.input_layer(features, fc.numeric_column('a'))

    self.evaluate(variables_lib.global_variables_initializer())
    self.evaluate(lookup_ops.tables_initializer())

    self.assertAllClose([[0.]], self.evaluate(net))
