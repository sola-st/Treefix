# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
price = fc.numeric_column('price', shape=2)
with ops.Graph().as_default():
    features = {'price': [[1., 2.], [5., 6.]]}
    net = fc_old.input_layer(features, [price])

    self.evaluate(variables_lib.global_variables_initializer())
    self.evaluate(lookup_ops.tables_initializer())

    self.assertAllClose([[1., 2.], [5., 6.]], self.evaluate(net))
