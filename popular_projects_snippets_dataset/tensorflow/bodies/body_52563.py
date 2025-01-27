# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
with ops.Graph().as_default():
    features = features = {'a': [0.], 'b': [1.]}
    columns = (fc.numeric_column(key) for key in features)
    net = fc_old.input_layer(features, columns)

    self.evaluate(variables_lib.global_variables_initializer())
    self.evaluate(lookup_ops.tables_initializer())

    self.assertAllClose([[0., 1.]], self.evaluate(net))
