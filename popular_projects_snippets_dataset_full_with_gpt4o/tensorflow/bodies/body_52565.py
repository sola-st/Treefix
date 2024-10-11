# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
price = fc.numeric_column('price')
with ops.Graph().as_default():
    features = {'price': [[1.], [5.]]}
    net = fc_old.input_layer(features, [price])

    self.evaluate(variables_lib.global_variables_initializer())
    self.evaluate(lookup_ops.tables_initializer())

    self.assertAllClose([[1.], [5.]], self.evaluate(net))
